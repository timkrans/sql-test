// Function to show a message on the page
function showMessage(message) {
    const messageDiv = document.getElementById('message');
    messageDiv.innerHTML = message; // Display message in the 'message' div
}

// Function to view all workouts
function viewWorkouts() {
    fetch('http://127.0.0.1:5001/workout', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        const workoutsList = document.getElementById('workouts-list');
        workoutsList.innerHTML = ''; // Clear previous workout list

        if (data.length === 0) {
            showMessage('No workouts found.');
        } else {
            showMessage('Here are the current workouts:');
            data.forEach(workout => {
                const workoutItem = document.createElement('div');
                workoutItem.innerHTML = `Workout: ${workout.workoutname}, Muscle Group: ${workout.musclegroup}, Equipment Used: ${workout.equipementused}, Video Link: <a href="${workout.videolink}" target="_blank">${workout.videolink}</a>`;
                workoutsList.appendChild(workoutItem);
            });
        }
    })
    .catch(error => {
        showMessage('Error fetching workouts.');
    });
}

// Function to add a workout (this is a mock-up; you can customize it with real data)
function addWorkout() {
    const newWorkout = {
        musclegroup: 'Arms',
        videolink: 'https://example.com/arm-workout-video',
        equipementused: 'Dumbbells',
        workoutname: 'Arm Day Routine'
    };

    fetch('http://127.0.0.1:5001/workout', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newWorkout),
    })
    .then(response => response.json())
    .then(data => {
        showMessage('Workout added successfully!');
        // After adding, you can re-fetch the workouts to see the updated list
        viewWorkouts();
    })
    .catch(error => {
        showMessage('Error adding workout.');
    });
}

// Function to delete a workout by its name
function deleteWorkout(workoutName) {
    fetch(`http://127.0.0.1:5001/workout/${encodeURIComponent(workoutName)}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === 'Workout not found') {
            showMessage('Workout not found!');
        } else {
            showMessage(`Workout "${workoutName}" deleted successfully.`);
        }
        // After deleting, re-fetch workouts to see the updated list
        viewWorkouts();
    })
    .catch(error => {
        showMessage('Error deleting workout.');
    });
}

// Event listeners for the buttons
document.getElementById('view-btn').addEventListener('click', viewWorkouts);
document.getElementById('add-btn').addEventListener('click', addWorkout);
document.getElementById('delete-btn').addEventListener('click', function() {
    deleteWorkout('Leg Day Routine');  // Example to delete a workout by name
});
