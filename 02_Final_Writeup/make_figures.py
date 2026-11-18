import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch
import os

OUT = "/home/user/CSC476_Semester_Project/02_Final_Writeup/figures"
os.makedirs(OUT, exist_ok=True)

def newfig(w=10, h=6.4):
    fig, ax = plt.subplots(figsize=(w, h), dpi=150)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
    return fig, ax

def save(fig, name):
    fig.savefig(os.path.join(OUT, name), bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", name)

def box(ax, x, y, w, h, text, fc="#EAF2FB", ec="#2C5F8A", fs=9, bold=False, rounded=True):
    if rounded:
        p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5", fc=fc, ec=ec, lw=1.4)
    else:
        p = Rectangle((x, y), w, h, fc=fc, ec=ec, lw=1.4)
    ax.add_patch(p)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=fs,
            fontweight="bold" if bold else "normal")

def arrow(ax, x1, y1, x2, y2, label=None, fs=7.6, color="#455A64", ls="-", lx=0, ly=1.8, both=False):
    style = "<|-|>" if both else "-|>"
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                 mutation_scale=12, color=color, lw=1.2, linestyle=ls))
    if label:
        ax.text((x1+x2)/2 + lx, (y1+y2)/2 + ly, label, ha="center", fontsize=fs,
                color="#333333", style="italic")

def line(ax, pts, color="#455A64", lw=1.2):
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=color, lw=lw)

def actor(ax, x, y, label):
    ax.add_patch(Circle((x, y+9), 3.0, fc="none", ec="#333333", lw=1.4))
    ax.plot([x, x], [y+6, y-3], color="#333333", lw=1.4)
    ax.plot([x-4.5, x+4.5], [y+1.5, y+1.5], color="#333333", lw=1.4)
    ax.plot([x, x-4], [y-3, y-9.5], color="#333333", lw=1.4)
    ax.plot([x, x+4], [y-3, y-9.5], color="#333333", lw=1.4)
    ax.text(x, y-12, label, ha="center", va="top", fontsize=9, fontweight="bold")

def package(ax, x, y, w, h, title, items):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4", fc="#F5F9FF", ec="#2C5F8A", lw=1.3))
    ax.add_patch(Rectangle((x+0.3, y+h-4.8), w-0.6, 4.5, fc="#2C5F8A", ec="none"))
    ax.text(x+w/2, y+h-2.55, title, ha="center", va="center", fontsize=8.3, color="white", fontweight="bold")
    ax.text(x+w/2, y+(h-4.8)/2, items, ha="center", va="center", fontsize=7.3)

def process(ax, x, y, r, num, text):
    ax.add_patch(Circle((x, y), r, fc="#E6F4EA", ec="#2E7D32", lw=1.4))
    ax.text(x, y+r*0.45, num, ha="center", va="center", fontsize=9, fontweight="bold", color="#1B5E20")
    ax.text(x, y-r*0.45, text, ha="center", va="center", fontsize=7.0)

def datastore(ax, x, y, w, h, label, fs=8):
    ax.add_patch(Rectangle((x, y), w, h, fc="#F3E8F7", ec="#7B1FA2", lw=1.4))
    ax.plot([x+0.9, x+0.9], [y, y+h], color="#7B1FA2", lw=2.6)
    ax.text(x+w/2+1.6, y+h/2, label, ha="center", va="center", fontsize=fs)

def entity(ax, x, y, w, name, attrs):
    h = 5.2 + 3.1*len(attrs)
    ax.add_patch(Rectangle((x, y), w, h, fc="#FFFFFF", ec="#333333", lw=1.3))
    ax.add_patch(Rectangle((x, y+h-4.6), w, 4.6, fc="#37474F", ec="none"))
    ax.text(x+w/2, y+h-2.3, name, ha="center", va="center", fontsize=8.6, color="white", fontweight="bold")
    for i, ln in enumerate(attrs):
        ax.text(x+1.4, y+h-7.0-3.1*i, ln, ha="left", va="center", fontsize=6.6, family="monospace")
    return h

def classbox(ax, x, y, w, name, attrs, methods):
    h = 5.0 + 3.0*len(attrs) + 3.0*len(methods) + 1.2
    ax.add_patch(Rectangle((x, y), w, h, fc="#FFFFFF", ec="#333333", lw=1.3))
    ax.add_patch(Rectangle((x, y+h-4.4), w, 4.4, fc="#00695C", ec="none"))
    ax.text(x+w/2, y+h-2.2, name, ha="center", va="center", fontsize=9, color="white", fontweight="bold")
    yy = y + h - 6.6
    for a in attrs:
        ax.text(x+1.4, yy, a, ha="left", va="center", fontsize=6.6, family="monospace"); yy -= 3.0
    yy -= 0.8
    ax.plot([x+0.6, x+w-0.6], [yy+1.5, yy+1.5], color="#333333", lw=0.8)
    for m in methods:
        ax.text(x+1.4, yy, m, ha="left", va="center", fontsize=6.6, family="monospace"); yy -= 3.0
    return h

def mult(ax, x, y, txt, ha="center"):
    ax.text(x, y, txt, fontsize=7.2, fontweight="bold", color="#333333", ha=ha)

# ---------------- Figure 3.1: three-tier architecture ----------------
fig, ax = newfig()
box(ax, 18, 76, 64, 15, "PRESENTATION LAYER\nWeb browser — HTML5, CSS3, JavaScript (responsive UI)", fc="#E3F0FB", fs=9.5)
box(ax, 18, 44, 64, 22, "APPLICATION LAYER\nFlask web server (Python)\nRoutes / controllers  •  business logic  •  authentication and authorisation", fc="#E8F5E9", ec="#2E7D32", fs=9.5)
box(ax, 18, 12, 64, 15, "DATA LAYER\nSQLite database — users, tickets, ticket_updates, projects, tasks, field_reports", fc="#F3E8F7", ec="#7B1FA2", fs=9.5)
arrow(ax, 50, 76, 50, 66, "HTTP requests / responses", both=True, lx=17, ly=0)
arrow(ax, 50, 44, 50, 27, "SQL queries / results", both=True, lx=15, ly=0)
ax.text(50, 96, "Client: any device with a web browser", ha="center", fontsize=8.5, style="italic")
ax.text(50, 5, "Deployed on a local web server (Flask / any WSGI host)", ha="center", fontsize=8.5, style="italic")
save(fig, "fig3_1_architecture.png")

# ---------------- Figure 3.2: use-case diagram ----------------
fig, ax = newfig(10, 6.6)
actor(ax, 7, 88, "Staff (reporter)")
actor(ax, 7, 64, "Technician")
actor(ax, 7, 40, "Supervisor")
actor(ax, 7, 16, "Administrator")
package(ax, 30, 80, 27, 14, "Authentication", "Log in\nLog out")
package(ax, 30, 56, 27, 16, "Help Desk (Staff)", "Submit ticket\nView my tickets\nTrack ticket status")
package(ax, 30, 32, 27, 16, "Help Desk (Technician)", "Update ticket status\nAdd comment\nClose ticket")
package(ax, 30, 6, 27, 14, "Administration", "Manage users\nManage categories")
package(ax, 66, 68, 30, 20, "Project Tracking", "Create project\nCreate task\nAssign task\nUpdate task progress\nMonitor progress")
package(ax, 66, 48, 30, 14, "Field Reporting", "File field report\nView field reports")
package(ax, 66, 26, 30, 14, "Dashboard and Reports", "View dashboard\nGenerate reports")
line(ax, [(11.5, 90), (30, 88)])
line(ax, [(11.5, 84), (30, 64)])
line(ax, [(11.5, 66), (30, 86)])
line(ax, [(11.5, 60), (30, 42)])
line(ax, [(11.5, 58), (24, 58), (24, 52), (66, 52)])
line(ax, [(11.5, 62), (26, 62), (26, 78), (66, 78)])
line(ax, [(11.5, 42), (30, 82)])
line(ax, [(11.5, 38), (21, 38), (21, 74), (66, 74)])
line(ax, [(11.5, 34), (21, 34), (21, 30), (66, 30)])
line(ax, [(11.5, 18), (30, 82)])
line(ax, [(11.5, 14), (30, 13)])
line(ax, [(11.5, 10), (18, 10), (18, 28), (66, 28)])
save(fig, "fig3_2_usecase.png")

# ---------------- Figure 3.3: Level-0 DFD ----------------
fig, ax = newfig()
box(ax, 3, 76, 17, 10, "Staff /\nReporter", fc="#FFF3E0", ec="#E65100", rounded=False, fs=8)
box(ax, 3, 44, 17, 10, "Technician", fc="#FFF3E0", ec="#E65100", rounded=False, fs=8)
box(ax, 3, 12, 17, 10, "Supervisor", fc="#FFF3E0", ec="#E65100", rounded=False, fs=8)
process(ax, 42, 80, 10, "1.0", "Help Desk\nTicketing")
process(ax, 42, 46, 10, "2.0", "Project\nTracking")
process(ax, 42, 12, 10, "3.0", "Field\nReporting")
process(ax, 74, 46, 10, "4.0", "Dashboard\nand Reports")
datastore(ax, 76, 76, 21, 13, "D1\nMaintenance\nDatabase", fs=7.6)
arrow(ax, 20, 81, 32, 80, "fault report / ticket", ly=2.4)
arrow(ax, 32, 76, 20, 75, "ticket status", ly=-3.0)
arrow(ax, 20, 49, 34, 71, "status updates", lx=-4, ly=2)
arrow(ax, 20, 14, 32, 12, "field report", ly=2.4)
arrow(ax, 20, 16, 32, 44, "project / task data", lx=-7, ly=0)
arrow(ax, 20, 10, 64, 40, "report requests", lx=-14, ly=0)
arrow(ax, 64, 42, 20, 8, "summary reports", lx=10, ly=0)
arrow(ax, 52, 82, 76, 82, "store / retrieve tickets", ly=2.4)
arrow(ax, 48, 52, 76, 74, "store / retrieve projects", lx=7, ly=2)
line(ax, [(48, 14), (60, 14), (60, 80), (76, 80)])
ax.text(58, 47, "store reports", fontsize=7.4, style="italic", color="#333333", rotation=90, ha="center", va="center")
arrow(ax, 82, 76, 78, 57, "query results", lx=9, ly=0)
save(fig, "fig3_3_dfd0.png")

# ---------------- Figure 3.4: ERD ----------------
fig, ax = newfig(10, 7)
entity(ax, 3, 62, 27, "USERS", ["PK  user_id", "    name", "    email (unique)", "    password_hash", "    role", "    created_at"])
entity(ax, 38, 48, 28, "TICKETS", ["PK  ticket_id", "    title", "    description", "    category", "    priority", "    status", "FK  reporter_id", "FK  technician_id", "    created_at", "    updated_at", "    resolved_at"])
entity(ax, 74, 58, 23, "TICKET_UPDATES", ["PK  update_id", "FK  ticket_id", "FK  author_id", "    note", "    old_status", "    new_status", "    created_at"])
entity(ax, 3, 6, 27, "PROJECTS", ["PK  project_id", "    name", "    description", "    start_date", "    end_date", "    status", "FK  created_by"])
entity(ax, 38, 6, 28, "TASKS", ["PK  task_id", "FK  project_id", "    title", "    description", "FK  assignee_id", "    deadline", "    status", "    progress (%)"])
entity(ax, 74, 6, 23, "FIELD_REPORTS", ["PK  report_id", "FK  technician_id", "FK  ticket_id (opt.)", "    location", "    equipment", "    findings", "    action_taken", "    report_date", "    created_at", "    status"])
# relationships
line(ax, [(30, 78), (38, 78)]); mult(ax, 30.8, 80.4, "1"); mult(ax, 37.2, 80.4, "N", ha="right"); ax.text(34, 74.6, "reports", fontsize=6.6, ha="center", style="italic", color="#555555")
line(ax, [(30, 70), (38, 70)]); mult(ax, 30.8, 72.4, "1"); mult(ax, 37.2, 72.4, "N", ha="right"); ax.text(34, 66.6, "assigned to", fontsize=6.6, ha="center", style="italic", color="#555555")
line(ax, [(66, 76), (74, 76)]); mult(ax, 66.8, 78.4, "1"); mult(ax, 73.2, 78.4, "N", ha="right"); ax.text(70, 72.6, "has", fontsize=6.6, ha="center", style="italic", color="#555555")
line(ax, [(16, 62), (16, 32.9)]); mult(ax, 14.2, 59.5, "1"); mult(ax, 17.8, 35.4, "N"); ax.text(20.5, 47, "creates", fontsize=6.6, ha="left", style="italic", color="#555555")
line(ax, [(30, 20), (38, 20)]); mult(ax, 30.8, 22.4, "1"); mult(ax, 37.2, 22.4, "N", ha="right"); ax.text(34, 16.6, "contains", fontsize=6.6, ha="center", style="italic", color="#555555")
line(ax, [(24, 62), (24, 44), (52, 44), (52, 36)]); mult(ax, 22.2, 59.5, "1"); mult(ax, 50.2, 38.4, "N"); ax.text(38, 46.4, "assigned to", fontsize=6.6, ha="center", style="italic", color="#555555")
line(ax, [(9, 62), (9, 2.5), (85, 2.5), (85, 6)]); mult(ax, 7.2, 59.5, "1"); mult(ax, 87.8, 3.8, "N"); ax.text(34, 4.9, "files", fontsize=6.6, ha="center", style="italic", color="#555555")
line(ax, [(66, 55), (70.5, 55), (70.5, 30), (74, 30)]); mult(ax, 68.2, 57.6, "0..1")
save(fig, "fig3_4_erd.png")

# ---------------- Figure 3.5: class diagram ----------------
fig, ax = newfig(10, 7)
classbox(ax, 4, 56, 28, "User", ["- user_id: int", "- name: str", "- email: str", "- password_hash: str", "- role: str"], ["+ login()", "+ logout()"])
classbox(ax, 36, 56, 28, "Ticket", ["- ticket_id: int", "- title: str", "- category: str", "- priority: str", "- status: str", "- reporter_id: int", "- technician_id: int"], ["+ assign(tech)", "+ update_status(s)", "+ close()"])
classbox(ax, 68, 56, 28, "TicketUpdate", ["- update_id: int", "- ticket_id: int", "- author_id: int", "- note: str", "- old_status: str", "- new_status: str"], ["+ add_note()"])
classbox(ax, 4, 6, 28, "Project", ["- project_id: int", "- name: str", "- start_date: date", "- end_date: date", "- status: str", "- created_by: int"], ["+ add_task()", "+ progress(): int"])
classbox(ax, 36, 6, 28, "Task", ["- task_id: int", "- project_id: int", "- title: str", "- assignee_id: int", "- deadline: date", "- status: str", "- progress: int"], ["+ update_progress(p)"])
classbox(ax, 68, 6, 28, "FieldReport", ["- report_id: int", "- technician_id: int", "- ticket_id: int (opt.)", "- location: str", "- equipment: str", "- findings: str", "- action_taken: str", "- report_date: date"], ["+ submit()"])
line(ax, [(32, 74), (36, 74)]); mult(ax, 32.7, 76.4, "1"); mult(ax, 35.3, 76.4, "N", ha="right"); ax.text(34, 71.2, "reports", fontsize=6.6, ha="center", style="italic", color="#555555")
line(ax, [(32, 64), (36, 64)]); mult(ax, 32.7, 66.4, "1"); mult(ax, 35.3, 66.4, "N", ha="right"); ax.text(34, 61.2, "assigned to", fontsize=6.6, ha="center", style="italic", color="#555555")
line(ax, [(64, 74), (68, 74)]); mult(ax, 64.7, 76.4, "1"); mult(ax, 67.3, 76.4, "N", ha="right"); ax.text(66, 71.2, "has", fontsize=6.6, ha="center", style="italic", color="#555555")
line(ax, [(18, 56), (18, 36.2)]); mult(ax, 16.3, 53.5, "1"); mult(ax, 19.7, 38.7, "N"); ax.text(21.5, 46, "creates", fontsize=6.6, ha="left", style="italic", color="#555555")
line(ax, [(32, 20), (36, 20)]); mult(ax, 32.7, 22.4, "1"); mult(ax, 35.3, 22.4, "N", ha="right"); ax.text(34, 17.2, "contains", fontsize=6.6, ha="center", style="italic", color="#555555")
line(ax, [(25, 56), (25, 50), (50, 50), (50, 36.2)]); mult(ax, 23.3, 53.5, "1"); mult(ax, 48.3, 38.7, "N"); ax.text(37, 52.4, "assigned to", fontsize=6.6, ha="center", style="italic", color="#555555")
line(ax, [(82, 56), (82, 39.2)]); mult(ax, 80.3, 53.5, "1"); mult(ax, 83.7, 41.7, "N"); ax.text(85.5, 47, "files", fontsize=6.6, ha="left", style="italic", color="#555555")
line(ax, [(64, 60), (66, 60), (66, 33), (68, 33)]); mult(ax, 66.9, 62.4, "0..1")
save(fig, "fig3_5_class.png")

# ---------------- Figure 3.6: login wireframe ----------------
fig, ax = newfig(7, 6)
ax.add_patch(Rectangle((8, 6), 84, 88, fc="#FFFFFF", ec="#546E7A", lw=1.6))
ax.add_patch(Rectangle((8, 86), 84, 8, fc="#CFD8DC", ec="#546E7A", lw=1.2))
for cx in (12, 16.5, 21):
    ax.add_patch(Circle((cx, 90), 1.4, fc="#90A4AE", ec="none"))
ax.text(50, 90, "maintenance-portal.local", ha="center", va="center", fontsize=7.5, color="#455A64")
ax.add_patch(FancyBboxPatch((28, 22), 44, 54, boxstyle="round,pad=0.6", fc="#F7FAFC", ec="#90A4AE", lw=1.2))
ax.text(50, 70, "MAINTENANCE DEPARTMENT", ha="center", fontsize=9.5, fontweight="bold", color="#1E3A5F")
ax.text(50, 65.5, "Help Desk • Projects • Field Reports", ha="center", fontsize=7.5, color="#546E7A")
ax.add_patch(Rectangle((33, 52), 34, 7, fc="#FFFFFF", ec="#B0BEC5", lw=1.1))
ax.text(35, 55.5, "Email address", ha="left", va="center", fontsize=7.5, color="#90A4AE")
ax.add_patch(Rectangle((33, 41), 34, 7, fc="#FFFFFF", ec="#B0BEC5", lw=1.1))
ax.text(35, 44.5, "Password", ha="left", va="center", fontsize=7.5, color="#90A4AE")
ax.add_patch(FancyBboxPatch((33, 30), 34, 7, boxstyle="round,pad=0.3", fc="#1E6BB8", ec="none"))
ax.text(50, 33.5, "LOG IN", ha="center", va="center", fontsize=8.5, color="white", fontweight="bold")
ax.text(50, 25.5, "Forgot password?", ha="center", fontsize=7, color="#1E6BB8")
ax.text(50, 15, "Roles: Staff • Technician • Supervisor • Administrator", ha="center", fontsize=7.5, style="italic", color="#546E7A")
save(fig, "fig3_6_wireframe_login.png")

# ---------------- Figure 3.7: dashboard wireframe ----------------
fig, ax = newfig(10, 6.4)
ax.add_patch(Rectangle((4, 4), 92, 92, fc="#FFFFFF", ec="#546E7A", lw=1.6))
ax.add_patch(Rectangle((4, 84), 92, 12, fc="#1E3A5F", ec="none"))
ax.text(7, 90, "MAINTENANCE PORTAL", fontsize=8.5, color="white", fontweight="bold", va="center")
ax.text(58, 90, "Tickets    Projects    Field Reports    Reports", fontsize=7.5, color="#CFD8DC", va="center")
ax.text(92, 90, "Logout", fontsize=7.5, color="#FFCDD2", va="center", ha="right")
ax.add_patch(Rectangle((4, 4), 24, 80, fc="#F0F4F8", ec="#CFD8DC", lw=1))
for i, item in enumerate(["Dashboard", "Tickets", "Projects", "Field Reports", "Reports", "Users"]):
    yy = 76 - i*10
    ax.add_patch(Rectangle((7, yy), 18, 7, fc="#1E6BB8" if i == 0 else "#FFFFFF", ec="#B0BEC5", lw=0.8))
    ax.text(16, yy+3.5, item, ha="center", va="center", fontsize=6.8, color="white" if i == 0 else "#1E3A5F")
cards = [("Open Tickets", "12"), ("Active Projects", "5"), ("Field Reports", "23")]
for i, (t, v) in enumerate(cards):
    x = 31 + i*21.5
    ax.add_patch(FancyBboxPatch((x, 66), 19, 14, boxstyle="round,pad=0.4", fc="#F7FAFC", ec="#90A4AE", lw=1.1))
    ax.text(x+9.5, 75.5, t, ha="center", fontsize=7.2, color="#546E7A")
    ax.text(x+9.5, 69.5, v, ha="center", fontsize=13, fontweight="bold", color="#1E3A5F")
ax.add_patch(Rectangle((31, 34), 44, 28, fc="#FFFFFF", ec="#B0BEC5", lw=1.1))
ax.text(53, 58.5, "Tickets by status (chart)", ha="center", fontsize=7.2, color="#546E7A")
for i, hgt in enumerate([10, 16, 7, 13, 20]):
    ax.add_patch(Rectangle((35 + i*8, 38), 5, hgt, fc="#1E6BB8", ec="none"))
ax.add_patch(Rectangle((78, 34), 15, 28, fc="#FFFFFF", ec="#B0BEC5", lw=1.1))
ax.text(85.5, 58.5, "Recent", ha="center", fontsize=7.2, color="#546E7A")
for i in range(6):
    ax.plot([80, 91], [54 - i*4, 54 - i*4], color="#CFD8DC", lw=1.4)
ax.add_patch(Rectangle((31, 8), 62, 22, fc="#FFFFFF", ec="#B0BEC5", lw=1.1))
ax.text(62, 23, "Recent field reports (table)", ha="center", fontsize=7.2, color="#546E7A")
for i in range(4):
    ax.plot([34, 90], [19 - i*4, 19 - i*4], color="#E0E0E0", lw=1.4)
save(fig, "fig3_7_wireframe_dashboard.png")

# ---------------- Figure 4.x: screenshot placeholders ----------------
def placeholder(name, fname):
    fig, ax = newfig(9, 5)
    ax.add_patch(FancyBboxPatch((8, 12), 84, 76, boxstyle="round,pad=1", fc="#ECEFF1", ec="#90A4AE", lw=1.6, linestyle="--"))
    ax.text(50, 62, "SCREENSHOT PLACEHOLDER", ha="center", fontsize=13, fontweight="bold", color="#607D8B")
    ax.text(50, 50, name, ha="center", fontsize=10.5, color="#37474F")
    ax.text(50, 36, "Insert the actual screenshot of the running application here\nafter implementation and testing (Chapter Four).", ha="center", fontsize=8.5, color="#78909C", style="italic")
    save(fig, fname)

placeholder("Login page", "fig4_1_login.png")
placeholder("Dashboard (after login)", "fig4_2_dashboard.png")
placeholder("Ticket list page", "fig4_3_tickets.png")
placeholder("New ticket form", "fig4_4_new_ticket.png")
placeholder("Ticket detail / status update page", "fig4_5_ticket_detail.png")
placeholder("Projects list page", "fig4_6_projects.png")
placeholder("Field report form", "fig4_7_field_report.png")
placeholder("Reports page", "fig4_8_reports.png")

print("ALL FIGURES DONE")
