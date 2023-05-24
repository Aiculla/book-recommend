<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Apache License 2.0][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Aiculla/book-recommend">
  </a>

<h3 align="center">Read Roulette</h3>

  <p align="center">
    This project utilizes a Machine Learning model trained on a comprehensive books dataset to deliver personalized book recommendations to users based off a random selection of three books. With the front-end developed using Vue.js and the back-end powered by Django, this system offers tailored recommendations for each user.
    <br />
    <br />
    <a href="https://github.com/Aiculla/book-recommend/issues">Report Bug</a>
    ·
    <a href="https://github.com/Aiculla/book-recommend/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
     <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Book Recommendation UI][product-screenshot]


This project is a web-based book recommendation system. The system uses a Machine Learning model trained on a books dataset to recommend books to users. The front-end is built using Vue.js and the backend is developed using Django.The book recommendation system provides recommendations based on the book's title, author, and publisher. The project uses a Machine Learning model trained on the TF-IDF Vectorizer representation of the book dataset. The Nearest Neighbors algorithm is used to find similar books based on cosine similarity.

The project has three main endpoints:

init: This endpoint is responsible for initializing the system. It preprocesses the book dataset and trains the model.

coldStart: This endpoint returns a random set of three books from the dataset. This is particularly useful when the user first visits the system and no user preference is known yet.

nextThree: This endpoint receives a book's ISBN and returns three books that are most similar to it.




<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Django][Django]][Django-url]
* [![scikit-learn][scikit-learn]][scikit-learn-url]
* [![Vue][Vue.js]][Vue-url]
* [![Pandas][Pandas]][Pandas-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This guide will walk you through the process of setting up the Book-Recommend project on your local environment.

Before starting, you will need:

* Python version 3.10.6 or later
* Node.js version 20.0.0 or later

If you do not have the required versions, please update your Python and Node.js installations before proceeding. You can check your current versions by running these commands in your terminal or command line. 
  ```sh
  python --version
  node --version
  ```

Once you have the necessary versions of Python and Node.js, you can proceed with the setup process as detailed in the following steps.

### Step 1: Navigate to the Project Directory

In your terminal or command line, navigate to the project's root directory using the following command:

  ```sh
  cd book-recommend
  ```

### Step 2: Create a Python Virtual Environment

We will create a Python virtual environment to isolate the project dependencies. Use the following command:

  ```sh
 python -m venv venv
  ```

### Step 3: Activate the Virtual Environment

The command to activate the virtual environment differs based on your operating system.

For Linux or MacOS, use:
  ```sh
source venv/bin/activate
  ```
If you're using Windows, use:
  ```sh
venv\Scripts\activate
  ```
  
### Step 4: Install Python Packages

Now, navigate to the mysite directory and install the required Python packages:

For Linux or MacOS, use:
  ```sh
cd mysite
pip install -r requirements.txt
  ```
The requirements.txt file should cover all necessary packages, including Django, Django CORS headers, Pandas, and Scikit-Learn. However, if you need to install these packages manually, you can do so with the following commands:
  ```sh
pip install django
pip install django-cors-headers
pip install pandas
pip install scikit-learn
  ```

### Step 5: Run the Django Server

With all packages installed, you're ready to run the Django server:

For Linux or MacOS, use:
  ```sh
python manage.py runserver
  ```

### Step 6: Open a New Terminal and Set Up Vue.js

Open a new terminal or command line instance. Now, navigate to the recommend-client directory within the book-recommend project:
  ```sh
cd book-recommend/recommend-client
  ```

For the front end of the application, we will use Vue.js. Make sure you have Node.js installed, then install Vue CLI globally:
  ```sh
npm install -g @vue/cli
  ```
### Step 7: Install Project Dependencies

Now install the Node.js dependencies

  ```sh
npm install
  ```

### Step 8: Run the Vue.js Application

Finally, you can run the Vue.js application with:

  ```sh
npm run serve
  ```


<!-- LICENSE -->
## License

Distributed under the Apache 2.0 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Walid Muhammad - walidmuhammad1@gmail.com

Project Link: [https://github.com/Aiculla/book-recommend](https://github.com/Aiculla/book-recommend)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Aiculla/book-recommend.svg?style=for-the-badge
[contributors-url]: https://github.com/Aiculla/book-recommend/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Aiculla/book-recommend.svg?style=for-the-badge
[forks-url]: https://github.com/Aiculla/book-recommend/network/members
[stars-shield]: https://img.shields.io/github/stars/Aiculla/book-recommend.svg?style=for-the-badge
[stars-url]: https://github.com/Aiculla/book-recommend/stargazers
[issues-shield]: https://img.shields.io/github/issues/Aiculla/book-recommend.svg?style=for-the-badge
[issues-url]: https://github.com/Aiculla/book-recommend/issues
[license-shield]: https://img.shields.io/github/license/Aiculla/book-recommend.svg?style=for-the-badge
[license-url]: https://github.com/Aiculla/book-recommend/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/walidmuhammad1
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[scikit-learn]: https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white
[scikit-learn-url]: https://scikit-learn.org/stable/#
[Pandas]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[product-screenshot]: https://github.com/Aiculla/book-recommend/blob/main/images/Books_Screenshot.png