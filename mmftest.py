
from mapmyfitness import MapMyFitness
from pprint import pprint

mmf = MapMyFitness(api_key='y784cxj4bhya92pduyha4nerqrwjdzj4',access_token='bdd9731cad1aafc4ffc906712905be8f99892609')

# workouts_paginator = mmf.workout.search(user=9118467) #random user

workouts_paginator = mmf.workout.search(user=49843456) #som


x = workouts_paginator.page(1)
w = x[2]
print w.name	#works fine
pprint(w.time_series) #gets stuck