import json
import requests
from django.shortcuts import render, get_object_or_404
from base.models import *
from django.contrib.auth.forms import UserCreationForm

API_KEY = "kNgd9nv/8Zsv1phHt0lvrA==AqEBcOyUfSVpniDa"

def register(request):
	return render(request, 'register.html')

def home(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def services(request):
	return render(request, 'services.html')

def personalized_workout(request, body_part=None, equipment_tool=None):
    predefined_body_parts = ["back", "cardio", "chest", "lower arms", "lower legs", "neck", "shoulder", "upper arms"]
    equipment_tools = [
        "assisted", "band", "barbell", "body weight", "bosu ball", "cable", "dumbbell", "elliptical machine", 
        "ez barbell", "hammer", "kettlebell", "leverage machine", "medicine ball", "olympic barbell", 
        "resistance band", "roller", "rope", "skierg machine", "sled machine", "smith machine", 
        "stability ball", "stationary bike", "stepmill machine", "tire", "trap bar", 
        "upper body ergometer", "weighted", "wheel roller"
    ]
    
    if body_part and body_part not in predefined_body_parts:
        # Handle the case where an invalid body part is provided
        return render(request, 'services/personalized-workout.html', {'body_parts': predefined_body_parts, 'error_message': 'Invalid body part'})

    if equipment_tool and equipment_tool not in equipment_tools:
        # Handle the case where an invalid equipment tool is provided
        return render(request, 'services/personalized-workout.html', {'body_parts': predefined_body_parts, 'equipment_tools': equipment_tools, 'error_message': 'Invalid equipment tool'})

    headers = {
        "X-RapidAPI-Key": "3107e210c4msh320bc0e06280efbp10cd72jsn0a5782a2d4b3",
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }

    try:
        # Fetch body parts
        body_parts = predefined_body_parts
    except requests.RequestException as e:
        print(f"Error fetching body parts: {e}")
        body_parts = []

    exercises_data = []

    if body_part:
        try:
            # Fetch exercises for the selected body part
            rapidapi_exercises_url = f"https://exercisedb.p.rapidapi.com/exercises/bodyPart/{body_part}"
            exercises_response = requests.get(rapidapi_exercises_url, headers=headers)
            exercises_response.raise_for_status()
            exercises_data = exercises_response.json()

            # Check if the response is a list of exercises or a single exercise
            if isinstance(exercises_data, list):
                # List of exercises
                pass
            elif isinstance(exercises_data, dict):
                # Single exercise - convert to a list for consistency
                exercises_data = [exercises_data]
            else:
                # Unexpected response format
                exercises_data = []

        except requests.RequestException as e:
            print(f"Error fetching exercises based on body part: {e}")

    elif equipment_tool:
        try:
            # Fetch exercises for the selected equipment tool
            rapidapi_exercises_url = f"https://exercisedb.p.rapidapi.com/exercises/equipment/{equipment_tool}"
            exercises_response = requests.get(rapidapi_exercises_url, headers=headers)
            exercises_response.raise_for_status()
            exercises_data = exercises_response.json()

            # Check if the response is a list of exercises or a single exercise
            if isinstance(exercises_data, list):
                # List of exercises
                pass
            elif isinstance(exercises_data, dict):
                # Single exercise - convert to a list for consistency
                exercises_data = [exercises_data]
            else:
                # Unexpected response format
                exercises_data = []

        except requests.RequestException as e:
            print(f"Error fetching exercises based on equipment: {e}")

    return render(request, 'services/personalized-workout.html', {
        'body_parts': body_parts,
        'body_part': body_part,
        'exercises_data': exercises_data,
        'equipment_tools': equipment_tools,
        'selected_equipment_tool': equipment_tool,
    })

def get_single_exercise(exercise_id):
    headers = {
        "X-RapidAPI-Key": "3107e210c4msh320bc0e06280efbp10cd72jsn0a5782a2d4b3",
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }

    try:
        # Fetch exercise by ID
        rapidapi_exercise_url = f"https://exercisedb.p.rapidapi.com/exercises/exercise/{exercise_id}"
        exercise_response = requests.get(rapidapi_exercise_url, headers=headers)
        exercise_response.raise_for_status()
        exercise_data = exercise_response.json()

        return exercise_data

    except requests.RequestException as e:
        print(f"Error fetching exercise by ID: {e}")
        return None

def show_single_exercise(request, exercise_id):
    exercise_data = get_single_exercise(exercise_id)
    print(exercise_data)  # Add this line for debugging

    return render(request, 'services/single-exercise.html', {'exercise_data': exercise_data})

def eatSmart(request):
	if request.method == 'POST':
		query = request.POST['query']
		api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
		api_request = requests.get(api_url + query, headers = {'X-Api-Key': 'kNgd9nv/8Zsv1phHt0lvrA==AqEBcOyUfSVpniDa'})

		try:
			api = json.loads(api_request.content)
			print(api_request.content)
		except Exception as e:
			api = "There was an error"
			print(e)

		return render(request, 'services/eatSmart.html', {'api': api})
	else:
		return render(request, 'services/eatSmart.html', {'query': 'Enter a valid query'})

def trainers(request):
    trainers = Trainer.objects.filter(trainer_status="active")

    context = {
        'trainers': trainers
    }

    return render(request, 'trainers.html', context)

def contact(request):
	return render(request, 'contact.html')

def joinCommunity(request):
    return render(request, 'joinCommunity.html')