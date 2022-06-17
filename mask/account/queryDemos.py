#returns all memebrs  from team_task model table

team_task=Team_task.objects.all()

#(2)retruns firstid in the table
firstid=Team_task.objects.first()

#(3)retruns lastid in the table
lastid=Team_task.objects.last()

#(4)retruns sinagle team leader by name 
Team_leader=Team_task.objects.get(name='teja')

#(5)retruns single single team leader by id
team_leader=Team_task,objects.get(id=1023221)

#(6) retruns all task related to team_memberfrom team_model

firstTeam_task.objects.all()

#(7) return team_model

team_model=Team_model.objects.all()
#(8)
team_model=Team_Model.objects.filter(status="under review")

#returnin Team_models  id leats to gratest
least_idTogratest=Team_task.objects.all().order_by('id')
least_idTOgretast=Team_model.objects.all().order_by('id')


#returning Team_models id gratest to least

gratestToleast= Team_model.objects.all.order_by('-id')
