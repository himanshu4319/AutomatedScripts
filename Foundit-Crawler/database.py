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

def selection(data):
    try:
        executor.execute(f"Select * from scrapper.data where `url`={data[0]}")
        return True
    except:
        return False

# data=('https://www.foundit.in/job/structural-engineer-schneider-electric-gurgaon-gurugram-india-29864669?searchId=8436f4f1-5ff8-40f5-a74c-3c6130c96083', 'Structural Engineer', 'Structural Engineer', 'Schneider Electric', 'Permanent Job', '', '', 'Gurgaon / Gurugram,, India', '', 'Other', '', '7-9 Years', "Job Description\nJOB DESCRIPTION: Structural Engineer\n\nObjective/Mission:\n\nPrimarily to carry out structural calculations, design verifications and suggest advance structural schemes to ensure fast track and efficient construction. Understanding of complex structural engineering loads (Blast, Sea) and analysis methods. Review building structural drawings from suppliers to be in-line with project specification, relevant standards, and classifications and to ensure deliverables are achieved by due dates. Assist other project engineers where necessary. Support multiple projects and tendering tasks as required. Effective communication with client and suppliers is required.\n\nProvides technical designs to customer projects & services teams, by having good technical knowledge and knowhow in an application domain or subdomain;\nIdentifies and understands customer technical requirements related to his/her application domain/subdomain;\nApplies internal procedures, standards & best practices in autonomy, related to his/her application domain/subdomain;\nCommunicates results internally and to customers; Presents and arguments them during project technical reviews;\n\nScope and Environment\n\nWorks both in autonomy and in team work, with contribution to project or service teams technical solution designs.\n\nWorks mainly for internal project and service technical teams (i.e. for DPT, DQT, DCT job family codes) along all the customer installation lifecycle, with some direct interaction with external customers related to his/her application domain/subdomain.\n\nKey activities and Responsibility\n\nCustomer and/or Partner relationships:\n\nHas direct interaction with customers, in design phase but also especially during testing and commissioning activities. Understands customer specifications and needs related to application domain/subdomain..\n\nProject and Risk Management:\n\nKnows the fundamentals of Project Management so that he/she is aware of the Cost/Quality targets (mainly related to his/her work); identifies and alerts in case of any deviations from the standard scope of work related to application domain/subdomain; issues regular progress reports to the project team; detects technical variation order opportunities related to application domain/subdomain.\n\nTechnical knowledge and Engineering:\n\nRelated to application domain/subdomain, applies engineering best practices & standards; has solid knowledge of the product & system offers (internal & external) related to application domain; has specific technical & application skills related to application domain/subdomain; carries out detailed engineering work and provide associated reporting to project team members; knows and uses the methods & tools related to application domain/subdomain, and may participate in improvement workshops on those methods & tools.\n\nTraining and coaching:\n\nExchanges and shares your knowledge to peers; gather feedback from other application design engineers; participates in the development of training modules or presentations about application domain/subdomain.\n\nJob Related Experience:\n\nStructural steel design, transportable building and offshore structures design and blast design experience will be an advantage. Hands on experience of structural analysis software namely, SpaceGass/StaadPro and SACS. Experience in FEM software namely, Strand 7 or any FEM software. Experience in preparing detailed structural calculation report to submission to customer and Coordination with Suppliers and clients as required.\n\nBusiness Understanding:\n\nExperience of relevant local Standards relating to Buildings/ Structures and building codes (mandatory), international standards, offshore standards, and blast design standards, Skills in adopting to any overseas standards.\n\nOther Skills:\n\nCommunication with all levels of management in verbal and written form.\n\nAbility to read, interpret technical specifications and able to review drawings\n\nGood problem-solving skills.\n\nCustomer service orientated.\n\nProficient computer skills including MS Word, MS Excel and MS Access,\n\nAREAS OF RESPONSIBILITY\n\nProject Engineer Management\n\nI. Identification of project scope and key requirements in order to ensure project deliverables are achieved on time and in accordance with the relevant specifications.\n\nII. Manage the different stake holders, suppliers, internal and client.\n\nIII. Take responsibility for contract management from time of contract acceptance and establish a contract file in accordance with Schneider guidelines such that the contract runs to a smooth timetable\n\nIV. Review Contract Specification for understanding of Project deliverables\n\nV. Manage the information flow from supplier to client.\n\nVI. Develop project program dashboard and milestones\n\nVII. Regularly conduct internal reviews with other departments to ensure communication and timely action to plan\n\nVIII. Prepare variations, NOI's, RFI's, CR's & vetting correspondences submitted by the customers\n\nIX. Review supplier issued drawings and comments received from client to ensure they are in compliance with the current scope & specifications and identify scope change and integrate with internal design teams\n\nX. Attend all relevant Technical Tele-conferences with suppliers and clients.\n\nXI. Submit relevant progress reports to management\n\nRelationship Management\n\nMaintains and encourages appropriate communications and cooperation:\n\nI. within the GCP OPS & SO business.\n\nII. within the leadership team.\n\nIII. with customers / partners.\n\nIV. within Schneider Electric divisions and entities.\n\nCustomer management\n\nI. Effective coordination with internal and external stake holders (Senior Structural Engineers, Senior Project Engineers HVAC, F&G, Electrical, Tendering, Project Management, Quality and Testing team)\n\nII. Responding to internal and external customers within a timely manner.\n\nIII. Maintain professional relationships.\n\nIV. Determine client requirements.\n\nV. Provide feedback to management.\n\nVI. Being customer focused when completing work.\n\nQualifications\n\nQualifications\n\nEducation qualification and Experience:\n\nDegree qualification in the Civil or Structural Engineering field.\n\nMinimum 7 Years Experience In Relevant Field\n\nSchedule: Full-time\n\nReq: 008T94", 'Found it', 'customer service, FEM software, structural engineering loads, Staadpro, Ms Word, overseas standards, blast, structural calculations, sea, engineering best practices, spacegass, building codes, MS Access, structural analysis software, product & system offers, Strand 7, SACS, local Standards, design verifications, problem-solving skills, buildings/ Structures, Ms Excel')
# print(selection(data))
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
