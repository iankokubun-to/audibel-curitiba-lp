document.addEventListener('DOMContentLoaded', () => {
    let collectedData = {};

    // Handle single option selection
    const options = document.querySelectorAll('.quiz-option');
    options.forEach(option => {
        option.addEventListener('click', function(e) {
            e.preventDefault();
            const targetStep = this.getAttribute('data-target');
            const answer = this.getAttribute('data-answer');
            const progress = this.getAttribute('data-progress');
            
            const currentStepId = this.closest('.quiz-step').id;
            collectedData[currentStepId] = answer;

            updateProgress(progress);
            goToStep(targetStep);
        });
    });

    // Handle multiple option selection (Step 4)
    const multiOptions = document.querySelectorAll('.quiz-multi-option');
    const btnContinueStep4 = document.getElementById('btn-continue-step-4');

    if (multiOptions && btnContinueStep4) {
        multiOptions.forEach(option => {
            option.addEventListener('click', function(e) {
                e.preventDefault();
                // Toggle selected state visually
                this.classList.toggle('border-audibel-red');
                this.classList.toggle('bg-red-50');
                const icon = this.querySelector('.check-icon');
                if (icon) {
                    icon.classList.toggle('opacity-0');
                    icon.classList.toggle('opacity-100');
                }
                this.classList.toggle('selected'); // Logically track selection

                // Enable/Disable continue button
                const anySelected = document.querySelectorAll('.quiz-multi-option.selected').length > 0;
                if (anySelected) {
                    btnContinueStep4.classList.remove('opacity-50', 'cursor-not-allowed');
                    btnContinueStep4.removeAttribute('disabled');
                } else {
                    btnContinueStep4.classList.add('opacity-50', 'cursor-not-allowed');
                    btnContinueStep4.setAttribute('disabled', 'true');
                }
            });
        });

        // Handle Continue button for Step 4
        btnContinueStep4.addEventListener('click', function(e) {
            e.preventDefault();
            const selectedAnswers = [];
            document.querySelectorAll('.quiz-multi-option.selected').forEach(opt => {
                selectedAnswers.push(opt.getAttribute('data-answer'));
            });

            collectedData['step-4'] = selectedAnswers.join(', ');
            updateProgress('60%'); // the progress bar was updated to 60%
            goToStep('step-5');
        });
    }

    // Handle back button
    const backBtns = document.querySelectorAll('.back-btn');
    backBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const targetStep = this.getAttribute('data-target');
            const progress = this.getAttribute('data-progress');
            
            updateProgress(progress);
            goToStep(targetStep);
        });
    });

    // Update Progress Bar
    function updateProgress(percentage) {
        document.getElementById('quiz-progress').style.width = percentage;
    }

    // Step transition
    function goToStep(stepId) {
        document.querySelectorAll('.quiz-step').forEach(step => {
            step.classList.remove('active');
        });
        document.getElementById(stepId).classList.add('active');
    }

    // Final Form Submission
    const form = document.getElementById('lead-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const name = document.getElementById('lead-name').value;
            const phone = document.getElementById('lead-phone').value;
            
            collectedData['Nome'] = name;
            collectedData['WhatsApp'] = phone;

            // Emulação de envio para PipeLead/CRM
            console.log("=== NOVO LEAD PRE-QUALIFICADO CURITIBA ===");
            console.log(JSON.stringify(collectedData, null, 2));
            console.log("==========================================");

            // Mostra tela de sucesso
            updateProgress('100%');
            goToStep('step-7');
        });
    }
});
