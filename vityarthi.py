<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Healthminder</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@4.2.0/fonts/remixicon.css" rel="stylesheet">
    <meta name="theme-color" content="#0f766e">
    <style>
      :root{
        --color-primary: #0f766e;
        --color-primary-dark: #0b6b60;
        --color-primary-light: #def7ee;
        --color-text-dark: #0f172a;
        --color-text-muted: #64748b;
        --color-text-subtle: #94a3b8;
        --color-bg: #f8fafc;
        --color-card: #ffffff;
        --color-border: #e2e8f0;
        --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
        --shadow-md: 0 4px 18px rgba(12,38,32,0.03);
        --shadow-lg: 0 16px 32px rgba(15, 118, 110, 0.08);
        --radius: 12px;
        --max-width: 1200px;
        --gap: 24px;
        --transition: 200ms cubic-bezier(.2,.9,.2,1);
        font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        font-size: 16px;
        line-height: 1.5;
      }

      *{box-sizing:border-box}
      html,body{height:100%}
      body{
        margin:0;
        background: linear-gradient(180deg, var(--color-bg) 0%, #e9edf1 100%);
        color: var(--color-text-dark);
        -webkit-font-smoothing:antialiased;
        -moz-osx-font-smoothing:grayscale;
        padding:40px 20px;
      }

      .container{
        max-width:var(--max-width);
        margin:0 auto;
        padding:12px;
      }

      /* header */
      .header{
        display:flex;
        margin-bottom:24px;
      }
      .header-content {
          display: flex;
          align-items: center;
          gap: 16px;
          background: var(--color-card);
          border: 1px solid var(--color-border);
          padding: 16px 20px;
          border-radius: var(--radius);
          box-shadow: var(--shadow-sm);
      }

      .app-icon {
          font-size: 2.2rem;
          color: var(--color-primary);
      }

      .app-title{
        margin:0;
        font-weight:700;
        font-size: 1.65rem;
        color: var(--color-primary-dark);
      }
      .lead{
          margin: 4px 0 0;
          color: var(--color-text-muted);
          font-weight: 500;
          font-size: 0.95rem;
      }

      /* layout */
      .grid{
        display:grid;
        grid-template-columns: 1fr;
        gap:var(--gap);
        align-items:start;
      }
      @media(min-width:980px){
        .grid{ grid-template-columns: 440px 1fr; align-items:start; gap:32px; }
      }

      /* global cards */
      .card{
        background:var(--color-card);
        border-radius:var(--radius);
        padding: 24px;
        box-shadow: 0 10px 30px rgba(15, 118, 110, 0.05);
        border:1px solid var(--color-border);
        transition: transform var(--transition), box-shadow var(--transition);
      }
      .card:hover{
          transform: translateY(-2px);
          box-shadow: 0 15px 35px rgba(12,38,32,0.08);
      }

      /* form */
      .form-card .card-title, .list-card .card-title{
        margin:0 0 16px 0;
        font-size:1.15rem;
        font-weight: 600;
        color: var(--color-text-dark);
        display: flex;
        align-items: center;
        gap: 8px;
      }
      .form-row{ margin-bottom: 18px; display:flex; flex-direction:column; gap:8px;}
      .form-row label{ font-weight:600; font-size:0.95rem; color: var(--color-text-dark);}
      .muted{ color:var(--color-text-muted); font-weight: 400; }
      .small{ font-size:0.875rem; }

      input[type="text"],
      input[type="date"],
      input[type="time"],
      textarea,
      select{
        border:1px solid var(--color-border);
        padding:12px 14px;
        border-radius:8px;
        font-size:0.96rem;
        background:linear-gradient(180deg,#fff,#fcfcfd);
        outline:none;
        transition:box-shadow .14s, border-color .14s;
        color: var(--color-text-dark);
      }
      textarea{ resize:vertical; min-height:80px; }
      input::placeholder, textarea::placeholder{ color: var(--color-text-subtle); opacity: 0.7; }

      input:focus, textarea:focus, select:focus{
        border-color: var(--color-primary);
        box-shadow: 0 0 0 3px var(--color-primary-light);
        transform: none;
      }

      /* split inputs */
      .split{ display:flex; gap:12px; }
      .split > div{ flex:1; }

      /* actions */
      .form-actions{ display:flex; justify-content:flex-end; gap:10px; margin-top:10px; }

      /* Base Button Styling */
      .btn-primary, .btn-secondary {
          padding: 10px 18px;
          border-radius: 10px;
          font-weight: 600;
          cursor: pointer;
          transition: transform .1s ease, background .15s, box-shadow .15s;
          display: flex;
          align-items: center;
          gap: 6px;
          font-size: 0.95rem;
          line-height: 1;
      }

      .btn-primary{
        background: var(--color-primary);
        color:#fff;
        border:none;
        box-shadow: 0 8px 20px rgba(15,118,110,0.2);
      }
      .btn-primary:hover{
          background: var(--color-primary-dark);
          transform:translateY(-1px);
          box-shadow: 0 12px 25px rgba(11,107,96,0.15);
      }

      .btn-secondary{
        background: var(--color-card);
        border:1px solid var(--color-border);
        color: var(--color-text-dark);
        box-shadow: var(--shadow-sm);
      }
      .btn-secondary:hover {
          background: var(--color-bg);
          transform: translateY(-1px);
      }

      
      .list-card{ padding-bottom: 20px; }
      .reminder-list{ display:flex; flex-direction:column; gap:16px; margin-top:12px; min-height:60px; }

      
      .reminder{
        display:flex;
        justify-content:space-between;
        gap:16px;
        align-items:center;
        padding:14px 16px;
        border-radius:var(--radius);
        background:linear-gradient(180deg,#ffffff,#faffff);
        border:1px solid rgba(11,107,96,0.06);
        position:relative;
        transition: transform var(--transition), box-shadow var(--transition);
      }
     
      .reminder::before{
        content: "";
        position:absolute;
        left:0; top:0; bottom:0;
        width:6px;
        background: var(--color-primary);
        border-top-left-radius:var(--radius);
        border-bottom-left-radius:var(--radius);
      }
      .reminder .meta{ display:flex; gap:16px; align-items:center; margin-left:8px; flex-grow:1; }
      .reminder .type{
        width:48px;height:48px;border-radius:10px;
        display:grid;place-items:center;font-weight:700;color: var(--color-primary-dark);
        background: var(--color-primary-light);
        flex-shrink:0;
        box-shadow: 0 4px 10px rgba(15,118,110,0.1);
        font-size: 1.3rem;
      }

      
      .reminder[data-type="medication"] .type { color: #d97706; background: #fef3c7; }
      .reminder[data-type="appointment"] .type { color: #10b981; background: #d1fae5; }
      .reminder[data-type="exercise"] .type { color: #ef4444; background: #fee2e2; }

      .reminder .info{
          display:flex;
          flex-direction:column;
          overflow: hidden;
      }
      .reminder .title{
          font-weight:700;
          font-size:1.05rem;
          color: var(--color-text-dark);
          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
      }
      .reminder .time{
          color: var(--color-text-subtle);
          font-size:0.9rem;
          margin-top:4px;
      }

      .reminder .actions{
          display:flex;
          gap: 6px;
          align-items:center;
          flex-shrink: 0;
      }
      .icon-btn{
        background:transparent;border:none;padding:8px;border-radius:8px;cursor:pointer;color: var(--color-text-muted);
        transition: background .12s, color .12s, transform .08s;
        font-size: 1.1rem;
      }
      .icon-btn:hover{
          background: var(--color-primary-light);
          color: var(--color-primary-dark);
          transform:translateY(-1px);
      }

      /* completed state */
      .reminder.completed{
          opacity:0.6;
          filter:grayscale(0.1);
          border-color: var(--color-border);
      }
      .reminder.completed::before {
          background: var(--color-text-subtle);
      }
      .reminder.completed .title{
          text-decoration:line-through;
          opacity:0.8;
      }

      /* empty note */
      #empty-note{
          padding:16px;
          margin-top:12px;
          border-radius:10px;
          background: linear-gradient(180deg,#fcfcfd,#fff);
          border:1px dashed var(--color-border);
          text-align: center;
      }

      /* footer */
      .footer{
          margin-top:30px;
          text-align:center;
          color:var(--color-text-muted);
      }

      /* Accessibility & small screens */
      :focus-visible {
          outline: none;
          box-shadow: 0 0 0 3px var(--color-primary-light);
          border-radius:8px;
      }
      a, button{ font-family:inherit; }

      @media (max-width:768px){
          body { padding: 20px 10px; }
          .header-content { padding: 12px 16px; }
          .app-title { font-size: 1.4rem; }
          .lead { font-size: 0.85rem; }
          .card { padding: 18px; }
          .form-card { order: 2; }
          .list-card { order: 1; }
          .reminder .meta { gap: 10px; }
          .reminder .type { width: 40px; height: 40px; font-size: 1.1rem; }
      }
    </style>
</head>
<body>
    <main class="container" role="main">
        <header class="header">
            <div class="header-content">
                <i class="ri-heart-pulse-fill app-icon"></i>
                <div>
                    <h1 class="app-title">Healthminder</h1>
                    <p class="lead">Keep track of medications, **appointments, and other health routines.</p>
                </div>
            </div>
        </header>

        <section class="panel grid">
            <form id="reminder-form" class="card form-card" aria-labelledby="add-reminder-title" novalidate>
                <h2 id="add-reminder-title" class="card-title"><i class="ri-add-line"></i> Add New Reminder</h2>

                <div class="form-row">
                    <label for="item-name">Name <span class="muted">(e.g. Blood Pressure Med)</span></label>
                    <input type="text" id="item-name" name="name" placeholder="e.g. Lisinopril" required autocomplete="off">
                </div>

                <div class="form-row">
                    <label for="item-details">Details <span class="muted">(dosage or location)</span></label>
                    <textarea id="item-details" name="details" rows="2" placeholder="e.g. 20mg, after breakfast or Dr. Smith's office" required></textarea>
                </div>

                <div class="form-row split">
                    <div>
                        <label for="item-date">Date</label>
                        <input type="date" id="item-date" name="date" required>
                    </div>
                    <div>
                        <label for="item-time">Time</label>
                        <input type="time" id="item-time" name="time" required>
                    </div>
                </div>

                <div class="form-row">
                    <label for="item-type">Type</label>
                    <select id="item-type" name="type">
                        <option value="medication">Medication (💊)</option>
                        <option value="appointment">Appointment (🗓)</option>
                        <option value="exercise">Exercise (🏃)</option>
                        <option value="other">Other (💡)</option>
                    </select>
                </div>

                <div class="form-actions">
                    <button type="button" class="btn-secondary" id="cancel-edit" hidden>Cancel</button>
                    <button type="submit" class="btn-primary" id="submit-btn">
                        <i class="ri-add-circle-line"></i> Add Reminder
                    </button>
                </div>
            </form>

            <section class="card list-card" aria-labelledby="upcoming-title">
                <h2 id="upcoming-title" class="card-title"><i class="ri-alarm-line"></i> Upcoming Reminders</h2>
                <div id="reminder-list" class="reminder-list" aria-live="polite"></div>
                <p id="empty-note" class="muted small">No reminders yet. Add one using the form on the left.</p>
            </section>
        </section>

        <footer class="footer">
            <small class="muted">A simple, focused health reminder app built with plain JavaScript.</small>
        </footer>
    </main>

    <script>
        const STORAGE_KEY = 'hm_reminders_v3';

        const form = document.getElementById('reminder-form');
        const listEl = document.getElementById('reminder-list');
        const emptyNote = document.getElementById('empty-note');
        const submitBtn = document.getElementById('submit-btn');
        const cancelBtn = document.getElementById('cancel-edit');

        let reminders = [];
        let editingId = null;

        // --- Utility Functions ---

        function readFromStorage() {
            try {
                const raw = localStorage.getItem(STORAGE_KEY);
                return raw ? JSON.parse(raw) : [];
            } catch (e) {
                console.warn("Failed to parse storage:", e);
                return [];
            }
        }

        function writeToStorage() {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(reminders));
        }

        function uid() {
            return Date.now().toString(16) + Math.random().toString(16).slice(2, 8);
        }

        function parseDatetime(dateStr, timeStr) {
            if (!dateStr) return null;
            const t = timeStr || '00:00';
            // Use local date string format for Date constructor
            const dt = new Date(${dateStr}T${t}:00);
            
            if (isNaN(dt.getTime())) return null;

            // Return ISO string
            return dt.toISOString();
        }

        function formatDatetime(isoStr) {
            if (!isoStr) return 'No specific time set';
            const dt = new Date(isoStr);
            if (isNaN(dt.getTime())) return 'Invalid Date/Time';
            
            // Format for display
            return dt.toLocaleString('en-US', {
                year: 'numeric',
                month: 'short',
                day: 'numeric',
                hour: 'numeric',
                minute: '2-digit'
            });
        }

        function getTypeIconAndValue(typeStr) {
            const typeMap = {
                'medication': { char: '💊', value: 'medication' },
                'appointment': { char: '🗓', value: 'appointment' },
                'exercise': { char: '🏃', value: 'exercise' },
                'other': { char: '💡', value: 'other' }
            };
            return typeMap[typeStr] || { char: '?', value: 'other' };
        }

        function sortReminders(r1, r2) {
            // 1. Completed status (false before true)
            const completion1 = r1.completed ? 1 : 0;
            const completion2 = r2.completed ? 1 : 0;
            if (completion1 !== completion2) {
                return completion1 - completion2;
            }

            // 2. Date (closest date first)
            const date1 = r1.datetime ? new Date(r1.datetime).getTime() : Infinity;
            const date2 = r2.datetime ? new Date(r2.datetime).getTime() : Infinity;

            return date1 - date2;
        }

        // --- Rendering Logic ---

        function render() {
            listEl.innerHTML = '';
            
            if (reminders.length === 0) {
                emptyNote.style.display = 'block';
                return;
            }
            emptyNote.style.display = 'none';

            // Sort reminders
            reminders.sort(sortReminders);

            reminders.forEach(r => {
                const { char, value } = getTypeIconAndValue(r.type || 'other');

                const item = document.createElement('div');
                item.className = reminder ${r.completed ? 'completed' : ''};
                item.setAttribute('data-type', value);

                item.innerHTML = `
                    <div class="meta">
                        <div class="type">${char}</div>
                        <div class="info">
                            <div class="title">${r.name || 'Untitled'}</div>
                            <div class="time">${formatDatetime(r.datetime) || (r.details || 'No details/date')}</div>
                        </div>
                    </div>
                    <div class="actions">
                        <button class="icon-btn toggle-done" title="${r.completed ? 'Mark as not done' : 'Mark as done'}" data-id="${r.id}">
                            <i class="${r.completed ? 'ri-refresh-line' : 'ri-check-line'}"></i>
                        </button>
                        <button class="icon-btn edit-btn" title="Edit" data-id="${r.id}">
                            <i class="ri-pencil-line"></i>
                        </button>
                        <button class="icon-btn delete-btn" title="Delete" data-id="${r.id}">
                            <i class="ri-delete-bin-line"></i>
                        </button>
                    </div>
                `;

                listEl.appendChild(item);
            });

            
            attachReminderEventListeners();
        }

        function attachReminderEventListeners() {
            listEl.querySelectorAll('.toggle-done').forEach(btn => {
                btn.addEventListener('click', (e) => toggleDone(e.currentTarget.dataset.id));
            });
            listEl.querySelectorAll('.edit-btn').forEach(btn => {
                btn.addEventListener('click', (e) => startEdit(e.currentTarget.dataset.id));
            });
            listEl.querySelectorAll('.delete-btn').forEach(btn => {
                btn.addEventListener('click', (e) => deleteReminder(e.currentTarget.dataset.id));
            });
        }

        function toggleDone(id) {
            const reminder = reminders.find(r => r.id === id);
            if (reminder) {
                reminder.completed = !reminder.completed;
                writeToStorage();
                render();
            }
        }

        function deleteReminder(id) {
            const reminder = reminders.find(r => r.id === id);
            if (!reminder) return;

            
            const shouldDelete = window.confirm(Are you sure you want to delete the reminder: '${reminder.name}'?);
            
            if (shouldDelete) {
                reminders = reminders.filter(r => r.id !== id);
                writeToStorage();
                render();
            }
        }

      

        function resetForm() {
            editingId = null;
            form.reset();
            submitBtn.innerHTML = '<i class="ri-add-circle-line"></i> Add Reminder';
            cancelBtn.hidden = true;
            document.getElementById('add-reminder-title').innerHTML = '<i class="ri-add-line"></i> Add New Reminder';
        }

        function startEdit(id) {
            const r = reminders.find(x => x.id === id);
            if (!r) return;

            document.getElementById('item-name').value = r.name || '';
            document.getElementById('item-details').value = r.details || '';
            document.getElementById('item-type').value = r.type || 'other';

            if (r.datetime) {
                const dt = new Date(r.datetime);
                const localDate = dt.toISOString().slice(0, 10);
                const localTime = dt.toISOString().slice(11, 16);
                document.getElementById('item-date').value = localDate;
                document.getElementById('item-time').value = localTime;
            } else {
                document.getElementById('item-date').value = '';
                document.getElementById('item-time').value = '';
            }

            editingId = id;
            submitBtn.innerHTML = '<i class="ri-save-line"></i> Save Changes';
            cancelBtn.hidden = false;
            document.getElementById('add-reminder-title').innerHTML = '<i class="ri-edit-line"></i> Edit Reminder';
            document.getElementById('item-name').focus();
        }

        function handleSubmit(e) {
            e.preventDefault();

            const name = document.getElementById('item-name').value.trim();
            const details = document.getElementById('item-details').value.trim();
            const date = document.getElementById('item-date').value;
            const time = document.getElementById('item-time').value;
            const type = document.getElementById('item-type').value;

            if (!name) {
                
                window.alert('Please provide a name for the reminder.');
                return;
            }

            const dtIso = parseDatetime(date, time);
            const nowIso = new Date().toISOString();

            if (editingId) {
                // Edit existing reminder
                const index = reminders.findIndex(r => r.id === editingId);
                if (index !== -1) {
                    reminders[index] = {
                        ...reminders[index],
                        name: name,
                        details: details,
                        type: type,
                        datetime: dtIso,
                        updated: nowIso
                    };
                }
            } else {
                // Add new reminder
                const newObj = {
                    id: uid(),
                    name: name,
                    details: details,
                    type: type,
                    datetime: dtIso,
                    completed: false,
                    created: nowIso
                };
                reminders.push(newObj);
            }

            writeToStorage();
            render();
            resetForm();
        }

        // --- Initialization ---

        function init() {
            reminders = readFromStorage();
            render();

            form.addEventListener('submit', handleSubmit);
            cancelBtn.addEventListener('click', resetForm);
        }

        window.onload = init;
    </script>
</body>
</html>