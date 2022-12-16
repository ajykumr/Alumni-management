  // <script src="{% static '/js/dashboard.js' %}" charset="utf-8"></script>

  


const com = [
    'TCS',
    'Infosys',
    'Wipro',
    'HCL',
    "Tech Mahindra",
    'Oracle',
    'Microsoft',
    'L&T',
    "Mphasis",
    'Mindtree',
    'Accel',
    'Cognizant',
    'HSBC',
    'Google',
    'Facebook',
    'Apple',
    'Alphabet',
    'Samsung',
    'Zoho',
    'Adobe',
    'Brave',
    'Nokia'
 ]


 const des = [
     'Support Specialist',
     'Computer Programmer',
     'Quality assurance tester',
     'web developer',
     'IT technician',
     'System analyst',
     'Network Engineer',
     'User Experience designer',
     'Database Administrator',
     'computer scientist',
     'Software Engineer',
     'IT security Specialist',
     'Data scientist',
     'Web Administrator',
     'Applicatons Engineer',
     'Cloud System Engineer',
     'Product Engineer',
     'Product designer',
     'UX designer',
     'Web designer'
 ]


const year = [
    "2012",
    "2013",
    "2014",
    "2015",
    "2016",
    "2017",
    "2018",
    "2019",
    "2020",
    "2021",
    "2022",
]

const gender = [
    'Male',
    'Female'
]

let student =  ["Ajay Kumar",
"Amol Y ",
"Amrutha MV",
"Ashutosh Sharma",
"Beerappa k",
"Bharani AL" ,
"Bhavith MS" ,
"Bhavya HR" ,
"Chandan MB" ,
"Darshini T",
"Darshini Priya" ,
"Deekshith Gowda" ,
"Druva D",
"Gururaj Rai",
"H Jeevitha",
"Harshitha BS",
"Harshitha DS",
"Hemavathi R",
"Jagath Shankar" ,
"Jairam C",
"Jeethendra CS",
"Karun Kumar",
"Kavya HM",
"Kiran K",
"Kiran Kumar" ,
"Manasa K R",
"Manohar",
"Mithun NS",
"Monisha Prasad",
"Naina C",
"Nizba Fathima" ,
"Pooja K",
"Pooja MM" ,
"Prathik P" ,
"Priyanka HY" ,
"Pruthvi BP",
"Rakshitha HS" ,
"Rashmi MR",
"Rekha NS",
"Sanchitha T",
"Shashi kumar",
"Sinchana RJ",
"Sneha CC",
"Sowjanya BM",
"Spandana BG",
"Srusti AR",
"Suha Kulsum",
"Suraj HS",
"Vanitha BM" ,
"Varshitha Gowda" ,
"Veena SM",
"Yuvaraj HS",
"Vandana Pranavi",
"Vishak Kowndinya",
"Likitha N",
"Archana BC",
"Ashika KS",
"Bhavana AV",
"Esharani A",
"Madhura M" ,
"Meghana B" ,
"Nandini D",
"Poonam Y",
"Rajesh U",
"Rakesh H",
"Ramya LR",
"Ruchitha MB",
"Shreenivasa Prasad",
"Varun V"]


function fill(localCount) {
    const st = student[localCount].split(" ")
    const a = parseInt(Math.random()*12)
    if (localCount < 10) {
        document.getElementById("id_usn").value = `4GH19CS00${localCount}`
    }
    document.getElementById("id_usn").value = `4GH19CS00${localCount}`
    document.getElementById("id_firstname").value = st[0]
    document.getElementById("id_lastname").value = st[1]
     document.getElementById("id_email").value = st[0] + "@gmail.com"
    document.getElementById("id_phone").value = parseInt(Math.random() * 10000000000);
    document.getElementById("id_birthdate").value = new Date(randomDate('01/01/2002', '01/01/2000')).toISOString().slice(0, 10);
    document.getElementById("id_present_Employer").value = com[parseInt(Math.random()*23)]
    document.getElementById("id_present_Designation").value = des[parseInt(Math.random()*21)]
    document.getElementById("id_present_Employer_join_year").value = year[parseInt((Math.random()*(12-a)) + a)]
    document.getElementById("id_previous_Employer").value =  com[parseInt(Math.random()*23)]
    document.getElementById("id_previous_Designation").value = des[parseInt(Math.random()*21)]
    document.getElementById("id_previous_Employer_join_year").value = year[a]
    document.getElementById("id_pass_year").value = year[a]
    document.getElementById("id_gender").value = gender[1]
    document.getElementById("id_branch").value = "CS"
    document.getElementById("t-and-c-agree").checked = true;
    const tagsNo = ['menutoggler','csrfmiddlewaretoken','profile_pic', 'submit', 't-and-c-agree', ]
    document.querySelectorAll('input').forEach((item, i) => {
        if (!tagsNo.includes(item.id) & !tagsNo.includes(item.name)) {
            if (item.value == 'undefined') {
                    fill(localCount)
            }
        }
    });

}


function randomDate(date1, date2){
    function randomValueBetween(min, max) {
      return Math.random() * (max - min) + min;
    }
    var date1 = date1 || '01-01-1970'
    var date2 = date2 || new Date().toLocaleDateString()
    date1 = new Date(date1).getTime()
    date2 = new Date(date2).getTime()
    if( date1>date2){
        return new Date(randomValueBetween(date2,date1)).toLocaleDateString()
    } else{
        return new Date(randomValueBetween(date1, date2)).toLocaleDateString()

    }
}

function resetCount(count = 0) {
    window.localStorage.setItem('count', count);
    console.log("count reseted to", count);
}


localCount = window.localStorage.getItem('count');
console.log(localCount);
fill(localCount)
window.localStorage.setItem('count', ++localCount);
