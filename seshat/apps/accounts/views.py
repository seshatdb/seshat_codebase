from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Profile
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse, reverse_lazy

from .models import Seshat_Expert, Seshat_Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import Seshat_TaskForm
from django.views import generic


def accounts(request):
    return HttpResponse('<h1>Hello Accounts.</h1>')

@login_required
def profile(request):
    # all_vars = []
    # a_huge_context_data_dic = {}
            #my_data = m.objects.filter(polity = polity_id)
            #a_huge_context_data_dic[m.__name__ + "_for_polity"] = my_data
            # coooooooooooool
            # this gets all the potential keys
            #print("Data: ", dir(my_data[0]))
        # else:
        #     print(polity_id, ": ", m)


    verified_facts = 0
    all_facts = 0
    all_tasks_given = []
    user_profile_id = None
    if request.user.is_authenticated:
        user_profile_id = request.user.profile.id
    my_user = Profile.objects.get(pk = user_profile_id)
    try:
        for ct in ContentType.objects.all():
            m = ct.model_class()
            if m and m.__module__ == f"seshat.apps.crisisdb.models":
                #print(dir(m.objects.all()))
                for an_instance in m.objects.all():
                    all_facts = all_facts + 1
                    #print(dir(an_instance.curator.values()))
                    if an_instance.curator.values():
                        for curator_person in an_instance.curator.values():
                            if curator_person['user_id'] == my_user.id:
                                print(curator_person, "YOOOOOOOOOOha")
                                verified_facts += 1
        
                #print("__")
                #print(m.curators.values())
    except:
        print("BAd message")

    try:
        for task in Seshat_Task.objects.all():
            if task.giver.user.id == my_user.id:
                print(task.giver.user.id, my_user.id)
                all_tasks_given.append(task)
    except:
        print("OUT")
    #print(dir(my_user))
    #print(my_user_name.user_id)
    context = {
        "facts_verified_by_user": verified_facts,
        "all_facts": all_facts,
        'all_tasks_given': all_tasks_given
        }

    print(my_user)
    return render(request, 'registration/profile.html', context=context)

class Seshat_taskCreate(PermissionRequiredMixin, CreateView):
    model = Seshat_Task
    form_class = Seshat_TaskForm
    template_name = "registration/seshat_task/seshat_task_form.html"
    permission_required = 'catalog.can_mark_returned'

# class Seshat_taskUpdate(PermissionRequiredMixin, UpdateView):
#     model = Seshat_Task
#     form_class = Seshat_TaskForm
#     template_name = "registration/seshat_task/seshat_task_update.html"
#     permission_required = 'catalog.can_mark_returned'

# class Seshat_taskDelete(PermissionRequiredMixin, DeleteView):
#     model = Seshat_Task
#     success_url = reverse_lazy('seshat_tasks')
#     template_name = "core/delete_general.html"
#     permission_required = 'catalog.can_mark_returned'


# class Seshat_taskListView(generic.ListView):
#     model = Seshat_Task
#     template_name = "registration/seshat_task/seshat_task_list.html"
#     paginate_by = 10
        
class Seshat_taskDetailView(generic.DetailView):
    model = Seshat_Task
    template_name = "registration/seshat_task/seshat_task_detail.html"
