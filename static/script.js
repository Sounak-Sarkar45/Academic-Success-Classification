let currentSectionIndex = 0;
const sections = document.querySelectorAll('.form-section');
const loadingDiv = document.getElementById('loading');
const predictionResultDiv = document.getElementById('prediction-result');

// Object to store form data
const formData = {};

// Function to save data from the current section
function saveCurrentSectionData() {
    const inputs = sections[currentSectionIndex].querySelectorAll('input, select');
    inputs.forEach(input => {
        formData[input.id] = input.type === 'checkbox' ? input.checked : input.value;
    });
}

// Function to restore data to a section
function restoreSectionData(index) {
    const inputs = sections[index].querySelectorAll('input, select');
    inputs.forEach(input => {
        if (formData.hasOwnProperty(input.id)) {
            if (input.type === 'checkbox') {
                input.checked = formData[input.id];
            } else {
                input.value = formData[input.id];
            }
        }
    });
}

// Function to show a specific section
function showSection(index) {
    sections.forEach((section, i) => {
        section.classList.toggle('active', i === index);
    });
    restoreSectionData(index); // Restore data when the section is displayed
}

// Navigate to the previous section
function previousSection() {
    if (currentSectionIndex > 0) {
        saveCurrentSectionData(); // Save data before leaving the section
        currentSectionIndex--;
        showSection(currentSectionIndex);
    }
}

// Navigate to the next section
function nextSection() {
    if (currentSectionIndex < sections.length - 1) {
        saveCurrentSectionData(); // Save data before leaving the section
        currentSectionIndex++;
        showSection(currentSectionIndex);
    }
}

// Submit the form
function submitForm() {
    // Get form data
    const inputs = document.querySelectorAll('input, select');
    const inputData = {};
    inputs.forEach(input => {
        if (input.type === 'checkbox') {
            inputData[input.id] = input.checked ? 1 : 0;
        } else {
            inputData[input.id] = input.value;
        }
    });

    // Show loading indicator
    loadingDiv.style.display = 'block';

    // Send the data to the backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(inputData)
    })
    .then(response => response.json())
    .then(data => {
        // Hide loading indicator
        loadingDiv.style.display = 'none';

        // Show the modal with the prediction result
        const modal = document.getElementById('prediction-modal');
        const modalMessage = document.getElementById('modal-message');

        // Add emoji based on prediction
        if (data.prediction === 'Graduate') {
            modalMessage.textContent = `The student will : Graduate 🤩`;
        } else if (data.prediction === 'Enrolled') {
            modalMessage.textContent = `The student is : Enrolled 😁`;
        } else if (data.prediction === 'Dropout') {
            modalMessage.textContent = `The student will : Dropout 😓`;
        } else {
            modalMessage.textContent = `Error: Invalid prediction`;
        }

        modal.style.display = 'block';
    })
    .catch(error => {
        // Hide loading indicator
        loadingDiv.style.display = 'none';

        // Show the modal with the error message
        const modal = document.getElementById('prediction-modal');
        const modalMessage = document.getElementById('modal-message');
        modalMessage.textContent = `Error: ${error.message}`;
        modal.style.display = 'block';
    });
}

// Function to close the modal
function closeModal() {
    const modal = document.getElementById('prediction-modal');
    modal.style.display = 'none';
}

// Initialize the first section
showSection(currentSectionIndex);
