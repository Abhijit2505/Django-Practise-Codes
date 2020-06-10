from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('''
    <!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
  <meta charset="utf-8">
  <title>Abhijit's Personal Webpage</title>
  <style>
    body {
      background-color: white;
    }
    hr{
      border-style: none;
      border-top-style:dotted;
      border-color: grey;
      border-width:6px;
      height: 0px;
      width: 5%;
    }
  </style>
</head>
<body>
  <table cellspacing="20">
    <tr>
      <td>
        <h1>Abhijit Tripathy</h1>
        <i>
          Undergraduate Student<br />
          Department Of <a href="http://www.ggu.ac.in/schools/dept%20of%20english/dept_of_ComputerEngg_index.html">
            Computer Science and Engineering,
          </a><br />
          School Of Studies in Engineering and Technology,<br />
          <a href="http://www.ggu.ac.in/">Guru Ghasidas University</a>
          <br />
          Chattisgarh,India,495009<br />
        </i>
      </td>
    </tr>
  </table>
  <hr />
  <strong>
    <h2>About me </h2>
  </strong>
  <p>
    I am an aspiring Machine Learning Engineer and AI developer,having a keen
    interest in problem solving, data structures, algorithms, discrete mathematics,
    number theory and statistical analysis.
    Also I like to solve cryptographic problems and take part in coding challenges
    organised monthly on different competitive programming sites.
    Currently, I am in search of some machine learning projects to work
    in real-time and learn from them.
    <br />
    <br />
    <strong>My specialization interest include,</strong>
  <ol>
    <li>Computer Vision</li>
    <li>Robotics</li>
    <li>Machine Learning</li>
    <li>Artificial Intelligence</li>
    <li>Micro-Economics and stocks</li>
  </ol>
  <strong>My hobbies include,</strong>
  <ol>
    <li>Technical Content writing</li>
    <li>Graphics Designing</li>
    <li>Listen to Music</li>
    <li>Watching a Movie</li>
  </ol>
  Contact information - <a href="contact-information.html">Click Here</a>
  </p>
  <hr />
  <h2>Work Experience</h2>
  <center>
    <table border="1">
      <thead>
        <tr>
          <td>
            <em><strong>Time Period</strong></em>
          </td>
          <td>
            <em><strong>Job Description</strong></em>
          </td>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            Nov,2019 - Jan,2020
          </td>

          <td>
            Senior Executive, Codesense Event, Equilibrio-2020
          </td>
        </tr>
        <tr>
          <td>
            Nov,2019 - Jan,2020
          </td>
          <td>
            Junior Executive, Office and Finance Core Team, Equilibrio-2020
          </td>
        </tr>
        <tr>
          <td>
            Dec,2019 - Jan,2020
          </td>
          <td>
            Associate, Model Exhibition,Autonomous Team, Equilibrio-2020
          </td>
        </tr>
      </tbody>
    </table>
  </center>
  <hr />
  <h2>Skills</h2>
  <center>
    <table border="1">
      <thead>
        <tr>
          <td>
            <em><strong>Skill's Name</strong></em>
          </td>
          <td>
            <em><strong>Grip</strong></em>
          </td>
          <td>
            <em><strong>Skill's Name</strong></em>
          </td>
          <td>
            <em><strong>Grip</strong></em>
          </td>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            C++ Programming
          </td>
          <td>
            ⭐⭐⭐⭐⭐
          </td>
          <td>
            Technical Writing
          </td>
          <td>
            ⭐⭐⭐⭐⭐
          </td>
        </tr>
        <tr>
          <td>
            Python Programming
          </td>
          <td>
            ⭐⭐⭐⭐⭐
          </td>
          <td>
            Blogging
          </td>
          <td>
            ⭐⭐⭐⭐
          </td>
        </tr>
        </tr>
        <tr>
          <td>
            Machine Learning
          </td>
          <td>
            ⭐⭐⭐⭐
          </td>
          <td>
            Micro-Economics
          </td>
          <td>
            ⭐⭐⭐
          </td>
        </tr>
        </tr>
        <tr>
          <td>
            Web Development
          </td>
          <td>
            ⭐⭐⭐
          </td>
          <td>
            Git & Github
          </td>
          <td>
            ⭐⭐⭐⭐
          </td>
        </tr>

      </tbody>
    </table>
  </center>
<hr />
</body>
</html>
''')
