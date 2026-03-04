// ===== PROGRESS TRACKING (localStorage) =====

function getProgress() {
    const data = localStorage.getItem('sierra-prep-progress');
    return data ? JSON.parse(data) : { completedDays: [], completedExercises: {} };
}

function saveProgress(progress) {
    localStorage.setItem('sierra-prep-progress', JSON.stringify(progress));
}

// ===== DASHBOARD =====

function updateDashboard() {
    const progress = getProgress();
    const completed = progress.completedDays.length;
    const remaining = 20 - completed;

    // Count total exercises done
    let exerciseCount = 0;
    for (const key in progress.completedExercises) {
        exerciseCount += progress.completedExercises[key].length;
    }

    // Update stats
    const statCompleted = document.getElementById('stat-completed');
    const statRemaining = document.getElementById('stat-remaining');
    const statExercises = document.getElementById('stat-exercises');
    if (statCompleted) statCompleted.textContent = completed;
    if (statRemaining) statRemaining.textContent = remaining;
    if (statExercises) statExercises.textContent = exerciseCount;

    // Update progress bars
    const pct = (completed / 20) * 100;
    const heroFill = document.getElementById('hero-progress-fill');
    if (heroFill) heroFill.style.width = pct + '%';

    // Update day cards
    for (let d = 1; d <= 20; d++) {
        const check = document.getElementById('check-' + d);
        const card = document.querySelector('.day-card[data-day="' + d + '"]');
        if (check && progress.completedDays.includes(d)) {
            check.classList.add('done');
            if (card) card.classList.add('completed');
        }
    }

    updateNavProgress(completed);
}

function updateNavProgress(completed) {
    const pct = (completed / 20) * 100;
    const fill = document.getElementById('progress-fill');
    const text = document.getElementById('progress-text');
    if (fill) fill.style.width = pct + '%';
    if (text) text.textContent = completed + ' / 20 days';
}

// ===== DAY PAGE =====

function initDayPage(dayNum, exerciseCount) {
    const progress = getProgress();

    // Update nav progress
    updateNavProgress(progress.completedDays.length);

    // Update day complete button
    const btn = document.getElementById('btn-complete-day');
    if (btn && progress.completedDays.includes(dayNum)) {
        btn.textContent = 'Day ' + dayNum + ' Completed!';
        btn.classList.add('is-complete');
    }

    // Update exercise statuses
    const dayExercises = progress.completedExercises[dayNum] || [];
    for (let i = 0; i < exerciseCount; i++) {
        const status = document.getElementById('ex-status-' + dayNum + '-' + i);
        const card = status ? status.closest('.exercise-card') : null;
        const doneBtn = card ? card.querySelector('.btn-done') : null;

        if (dayExercises.includes(i)) {
            if (status) status.classList.add('done');
            if (card) card.classList.add('done');
            if (doneBtn) {
                doneBtn.textContent = 'Done!';
                doneBtn.classList.add('is-done');
            }
        }
    }
}

function toggleDayComplete(dayNum) {
    const progress = getProgress();
    const idx = progress.completedDays.indexOf(dayNum);
    const btn = document.getElementById('btn-complete-day');

    if (idx === -1) {
        progress.completedDays.push(dayNum);
        if (btn) {
            btn.textContent = 'Day ' + dayNum + ' Completed!';
            btn.classList.add('is-complete');
        }
    } else {
        progress.completedDays.splice(idx, 1);
        if (btn) {
            btn.textContent = 'Mark Day ' + dayNum + ' Complete';
            btn.classList.remove('is-complete');
        }
    }

    saveProgress(progress);
    updateNavProgress(progress.completedDays.length);
}

function toggleExercise(dayNum, exerciseIdx) {
    const progress = getProgress();
    if (!progress.completedExercises[dayNum]) {
        progress.completedExercises[dayNum] = [];
    }

    const exercises = progress.completedExercises[dayNum];
    const idx = exercises.indexOf(exerciseIdx);
    const status = document.getElementById('ex-status-' + dayNum + '-' + exerciseIdx);
    const card = status ? status.closest('.exercise-card') : null;
    const doneBtn = card ? card.querySelector('.btn-done') : null;

    if (idx === -1) {
        exercises.push(exerciseIdx);
        if (status) status.classList.add('done');
        if (card) card.classList.add('done');
        if (doneBtn) {
            doneBtn.textContent = 'Done!';
            doneBtn.classList.add('is-done');
        }
    } else {
        exercises.splice(idx, 1);
        if (status) status.classList.remove('done');
        if (card) card.classList.remove('done');
        if (doneBtn) {
            doneBtn.textContent = 'Mark Done';
            doneBtn.classList.remove('is-done');
        }
    }

    saveProgress(progress);
}

// ===== COLLAPSIBLE HINTS/SOLUTIONS =====

function toggleHint(btn) {
    const content = btn.nextElementSibling;
    const isOpen = content.classList.contains('open');
    content.classList.toggle('open');
    btn.textContent = isOpen ? 'Show Hint' : 'Hide Hint';
}

function toggleSolution(btn) {
    const content = btn.nextElementSibling;
    const isOpen = content.classList.contains('open');
    content.classList.toggle('open');
    btn.textContent = isOpen ? 'Show Solution' : 'Hide Solution';

    // Re-highlight code when opening
    if (!isOpen) {
        content.querySelectorAll('pre code').forEach(block => {
            hljs.highlightElement(block);
        });
    }
}
