import sqlite3

DB_FILE = "jobs.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT,
        role TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_job():
    company = input("Company: ")
    role = input("Role: ")
    status = input("Status (applied/interview/etc): ")

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO jobs (company, role, status) VALUES (?, ?, ?)",
        (company, role, status)
    )

    conn.commit()
    conn.close()

    print("Job saved!")


def list_jobs():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jobs")

    jobs = cursor.fetchall()

    for job in jobs:
        print(job)

    conn.close()


def menu():
    print("\nJob Tracker")
    print("1. Add job")
    print("2. List jobs")
    print("3. Update job status")
    print("4. Delete job")
    print("5. Filter jobs by status")
    print("6. Exit")


def main():
    init_db()

    while True:
        menu()
        choice = input("Select option: ")

        if choice == "1":
            add_job()
        elif choice == "2":
            list_jobs()
        elif choice == "3":
            update_job_status()
        elif choice == "4":
            delete_job()
        elif choice == "5":
            filter_jobs_by_status()
        elif choice == "6":
            break
        else:
            print("Invalid option")

       

def update_job_status():
    job_id = input("Enter job ID to update: ")
    new_status = input("New status: ")

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE jobs SET status = ? WHERE id = ?",
        (new_status, job_id)
    )

    conn.commit()
    conn.close()

    print("Job updated!")

def delete_job():
    job_id = input("Enter job ID to delete: ")

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
    conn.commit()
    conn.close()

    print("Job deleted!")

def filter_jobs_by_status():
    status = input("Enter status to filter by: ")

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jobs WHERE status = ?", (status,))
    jobs = cursor.fetchall()

    print(f"\n--- Jobs with status: {status} ---")
    for job in jobs:
        print(f"ID: {job[0]} | {job[1]} | {job[2]} | Status: {job[3]}")

    conn.close()
 


if __name__ == "__main__":
    main()