class HelpDeskSystem:
    def __init__(self):
        self.tickets = []

    def display_menu(self):
        print("--------------------------------------")
        print(" Welcome to Hospital Help Desk System")
        print("---------------------------------------")
        print("1. Report Issue")
        print("2. View Issues")
        print("3. Search Issue")
        print("4. Update Issue Status")
        print("5. Quit")

    def report_issue(self):
        print("-------------------------")
        print("Report New Issue")
        print("-------------------------")
        issue = {}
        issue['ticket_id'] = input("Enter Ticket ID: ")
        issue['department'] = input("Enter Department: ")
        issue['description'] = input("Enter Issue Description: ")
        issue['status'] = "Open"
        self.tickets.append(issue)
        print("Issue reported successfully")

    def view_issues(self):
        print("--- Issue Records ---")
        for ticket in self.tickets:
            print("Ticket ID:", ticket['ticket_id'])
            print("Department:", ticket['department'])
            print("Description:", ticket['description'])
            print("Status:", ticket['status'])
            print("-------------------------")

    def search_issue(self):
        ticket_id = input("Enter Ticket ID to search: ")
        for ticket in self.tickets:
            if ticket['ticket_id'] == ticket_id:
                print("Issue Found:")
                print("Ticket ID:", ticket['ticket_id'])
                print("Department:", ticket['department'])
                print("Description:", ticket['description'])
                print("Status:", ticket['status'])
                return
        print("Issue not found.")

    def update_issue_status(self):
        ticket_id = input("Enter Ticket ID to update: ")
        for ticket in self.tickets:
            if ticket['ticket_id'] == ticket_id:
                print("Update Issue Status")
                new_status = input("Enter new status: ")
                ticket['status'] = new_status
                print("Issue status updated successfully")
                return
        print("Issue not found.")

# Create an instance of the HelpDeskSystem
help_desk_system = HelpDeskSystem()

# Main loop for menu selection
while True:
    help_desk_system.display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        help_desk_system.report_issue()
    elif choice == '2':
        help_desk_system.view_issues()
    elif choice == '3':
        help_desk_system.search_issue()
    elif choice == '4':
        help_desk_system.update_issue_status()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")
