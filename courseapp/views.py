from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Question, Choice, Submission, Enrollment

def homepage(request):
    return render(request, 'homepage.html')

def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {'course': course}
    return render(request, 'course_details_bootstrap.html', context)

def submit_exam(request, course_id):
    if request.method == 'POST':
        user = request.user
        course = get_object_or_404(Course, pk=course_id)
        enrollment, created = Enrollment.objects.get_or_create(user=user, course=course)

        submission = Submission.objects.create(enrollment=enrollment)

        selected_choices = request.POST.getlist('choice')
        for choice_id in selected_choices:
            choice = get_object_or_404(Choice, pk=int(choice_id))
            submission.choices.add(choice)

        return HttpResponseRedirect(reverse('exam_result', args=(course.id, submission.id)))

def exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    selected_ids = submission.choices.values_list('id', flat=True)
    total = 0
    score = 0

    for question in course.question_set.all():
        total += question.grade
        correct_choices = question.choice_set.filter(is_correct=True).values_list('id', flat=True)
        selected_for_question = selected_ids.intersection(correct_choices)
        if set(correct_choices) == set(selected_for_question):
            score += question.grade

    context = {
        'course': course,
        'score': score,
        'total': total,
        'selected_ids': selected_ids
    }
    return render(request, 'exam_result.html', context)
