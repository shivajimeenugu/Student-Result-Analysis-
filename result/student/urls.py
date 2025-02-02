from django.urls import path

from . import views
urlpatterns = [
    # path('semester',views.SemView.as_view()),
    path('index',views.index, name="index"),
    # path('upload',views.upload,name="upload"),
    path('data',views.data,name="upload_data"),
    # path('backlog',views.backlogupload,name="backlog"),
    path('backpost',views.backlogdata,name="backlog_data"),
    path('subj/<int:sem_id>',views.get_sem_analysis,name="sem_data"),
    path('all-subj/<int:sem_id>',views.subj_analysis_all,name="all-subj-analysis"),
    path('student',views.student_detail,name="student"),
    path('student/<int:sem_id>',views.get_sect_analysis,name="student_data"),
    path('test',views.generate_list_semester, name="test"),
    path('updata',views.get_reg_branch_batch,name="updata"),
    path('backupdata',views.get_back_predata, name="backdata"),
    path('batch/<int:batch_id>/<int:branch_id>',views.get_batch_analysis,name="batch_data"),
    path('batch/sem/<int:batch_id>/<int:branch_id>',views.get_all_sems_backlog,name="Sem_backlog_data"),
    path('fetch_result/<str:roll>/<str:branch>/<int:sem>',views.fetch_result,name="fetch_result"), 
    path('fetch_semester_result/<int:batch>/<int:sem>/<str:branch>/',views.fetch_semester_result,name="fetch_semester_result"), 
    path('fetch_test/<int:num>',views.fetch_test,name="fetch_test"),
    path('cancel',views.cancel),
    path('get_topper_data/<int:batch>/<int:sem>/<str:branch>',views.get_topper_data,name="get_topper_data"),
    path('get_sec_wise_topper_data/<int:batch>/<int:sem>/<str:branch>/<int:sec>',views.get_sec_wise_topper_data,name="get_sec_wise_topper_data"),
]



 


