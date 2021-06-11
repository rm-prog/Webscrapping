from bs4 import BeautifulSoup
import requests

def find_job():
    # Open njoftime.com website that searches for job
    html_text = requests.get('https://www.njoftime.com/forumdisplay.php?14-ofroj-vende-pune&s=&pp=30&field3[0]=Tirane&field7[0]=20&field7[1]=2001&field7[2]=2000&field4_isMin=&field4_isMax=&input_titull=&daysprune=30')
    # Get content of website
    soup = BeautifulSoup(html_text.content, "lxml")
    # find div with class threadinfo
    # this div contains main info about job
    job = soup.find("div", class_ = "threadinfo")
    # find the first link with class title
    # this link takes you to the job offer page
    job_name = job.find("a", class_ = "title")
    # find link with class -------
    # this link represent company name
    company_name = job.find("a", class_ = "username offline popupctrl").text
    # from job_name get the link
    job_href = job_name['href']
    # go the job offer page through job_href link 
    job_page = requests.get(f'https://www.njoftime.com/{job_href}')
    # get the next page content
    soup1 = BeautifulSoup(job_page.content, "lxml")
    # get div with all info about job
    job_info_container = soup1.find("div", class_ = 'postcontent restore').text
    # save info to text file
    with open("info.txt", "w") as text_file:
        text_file.write(f"{company_name} offers {job_name.text}\n")    
        text_file.write(f" - {job_info_container}\n")


find_job()