import mysql.connector

conn = mysql.connector.connect(host="localhost",user="almabay",passwd="abc@1234",database="scrapper")
executor = conn.cursor()

def insertion(data):
    # print(data)
    try:
        executor.execute("Insert into data(`url`,`job_title`,`job_role`,`company`,`job_type`,`job_shift`,`job_salary`,`job_location`,`job_benefits`,`industry_type`,`education`,`experience`,`job_description`,`src`,`skills`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",data)
        conn.commit()
    except Exception as e:
        print(f"Exception {e}")


#Database need to be configured...



# CREATE TABLE scrapper.data (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     url TEXT,
#     job_title VARCHAR(255),
#     job_role VARCHAR(255),
#     company VARCHAR(255),
#     job_type VARCHAR(255),
#     job_shift VARCHAR(255),
#     job_salary VARCHAR(255),
#     job_location VARCHAR(255),
#     job_benefits TEXT,
#     industry_type TEXT,
#     education TEXT,
#     experience TEXT,
#     job_description TEXT,
#     src VARCHAR(255),
#     skills TEXT
#     );
