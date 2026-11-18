"""Capture real screenshots of the running application for Chapter Four."""
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:5000"
OUT = "/home/user/CSC476_Semester_Project/02_Final_Writeup/figures"


def login(page, email, password):
    page.goto(BASE + "/logout")
    page.goto(BASE + "/login")
    page.fill("#email", email)
    page.fill("#password", password)
    page.click("button[type=submit]")
    page.wait_for_load_state("networkidle")


with sync_playwright() as p:
    browser = p.chromium.launch()
    ctx = browser.new_context(viewport={"width": 1280, "height": 900})
    page = ctx.new_page()

    # Figure 4.1: login page (signed out)
    page.goto(BASE + "/logout")
    page.goto(BASE + "/login")
    page.wait_for_load_state("networkidle")
    page.screenshot(path=OUT + "/fig4_1_login.png", full_page=True)
    print("4.1 login")

    # Figure 4.2: dashboard (supervisor)
    login(page, "supervisor@maintenance.local", "supervisor123")
    page.goto(BASE + "/dashboard")
    page.wait_for_load_state("networkidle")
    page.screenshot(path=OUT + "/fig4_2_dashboard.png", full_page=True)
    print("4.2 dashboard")

    # Figure 4.3: ticket list (staff)
    login(page, "staff@maintenance.local", "staff123")
    page.goto(BASE + "/tickets")
    page.wait_for_load_state("networkidle")
    page.screenshot(path=OUT + "/fig4_3_tickets.png", full_page=True)
    print("4.3 tickets")

    # Figure 4.4: new ticket form (staff)
    page.goto(BASE + "/tickets/new")
    page.wait_for_load_state("networkidle")
    page.screenshot(path=OUT + "/fig4_4_new_ticket.png", full_page=True)
    print("4.4 new ticket")

    # Figure 4.5: ticket detail / status update (technician, ticket 1)
    login(page, "tech@maintenance.local", "tech123")
    page.goto(BASE + "/tickets/1")
    page.wait_for_load_state("networkidle")
    page.screenshot(path=OUT + "/fig4_5_ticket_detail.png", full_page=True)
    print("4.5 ticket detail")

    # Figure 4.6: projects list (supervisor)
    login(page, "supervisor@maintenance.local", "supervisor123")
    page.goto(BASE + "/projects")
    page.wait_for_load_state("networkidle")
    page.screenshot(path=OUT + "/fig4_6_projects.png", full_page=True)
    print("4.6 projects")

    # Figure 4.7: field report form (technician)
    login(page, "tech@maintenance.local", "tech123")
    page.goto(BASE + "/field-reports/new")
    page.wait_for_load_state("networkidle")
    page.screenshot(path=OUT + "/fig4_7_field_report.png", full_page=True)
    print("4.7 field report")

    # Figure 4.8: reports page (supervisor, with a filter applied)
    login(page, "supervisor@maintenance.local", "supervisor123")
    page.goto(BASE + "/summary?status=Open")
    page.wait_for_load_state("networkidle")
    page.screenshot(path=OUT + "/fig4_8_reports.png", full_page=True)
    print("4.8 reports")

    browser.close()

print("ALL SCREENSHOTS CAPTURED")
