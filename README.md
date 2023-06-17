<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL-3.0 License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/cargonvis/cheap_flights_search">
    <img src="images/plane.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">CHEAP FLIGHTS SEARCH</h3>

  <p align="center">
    This repository contains code for searching cheap flights using the Raspberry Pi Zero/Zero 2W.
    <br />
    <a href="https://github.com/cargonvis/cheap_flights_search"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/cargonvis/cheap_flights_search">View Demo</a>
    ·
    <a href="https://github.com/cargonvis/cheap_flights_search/issues">Report Bug</a>
    ·
    <a href="https://github.com/cargonvis/cheap_flights_search/issues">Request Feature</a>
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
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <!-- <li><a href="#usage">Usage</a></li> -->
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <li><a href="#future-improvements">Future Improvements</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) --> 
![Product Name Screen Shot][product-screenshot] <!-- Image without link -->

This project is a flight search application that helps you find the cheapest flight offers based on your search criteria. It uses the IATA and ICAO Codes API to retrieve information about airlines, and the Kiwi API for searching flights.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.org]][Python-url]
* [![Json][Json.org]][Json-url]
* [![Pandas][Pandas.org]][Pandas-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get started with this project, follow the steps below:

### Prerequisites

Run the following command to install the necessary libraries:
* install.sh
  ```
  ./install.sh
  ```

### Installation

1. Get a free IATA and ICAO API key from [RapidAPI](https://rapidapi.com/vacationist/api/iata-and-icao-codes/)
2. Get a free KIWI API key from [Tequila](https://tequila.kiwi.com/portal/getting-started)
3. Clone the repo:
   ```
   git clone https://github.com/cargonvis/cheap_flights_search.git
   ```
4. Email Configuration:
   To enable email notifications for the cheapest flights, you need to provide two email addresses:
   	- SENDER_EMAIL: Email address from which the mail will be sent. It is recommended to use a Gmail account. To grant Python code access to the sender email, you need to create an [App Password](https://support.google.com/accounts/answer/185833?hl=en).
	- RECEIVER_EMAIL: Email address that will receive the mail.
5. Replace Variables:
   In the code, replace the following variables at the top:
	- IATA_ICAO_API_KEY: Replace with your IATA and ICAO API key.
	- KIWI_API_KEY: Replace with your KIWI API key.
	- SENDER_EMAIL: Replace with the sender email address.
	- RECEIVER_EMAIL: Replace with the receiver email address.
	- APP_PASSWORD: Replace with the app password generated for the sender email.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
<!--## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_-->

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- ROADMAP -->
<!--## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature-->

See the [open issues](https://github.com/cargonvis/cheap_flights_search/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- FUTURE IMPROVEMENTS -->
## Future Improvements

- Implement additional notification systems such as SMS, WhatsApp, Telegram, etc.
- Include Seatguru API (or similar) for selecting the best seats on the cheapest flights.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

[![Email][Email-shield]][Email-url] [![LinkedIn][linkedin-shield]][linkedin-url] [![Discord][Discord-shield]][Discord-url]

Project Link: [https://github.com/cargonvis/cheap_flights_search](https://github.com/cargonvis/cheap_flights_search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!--## Acknowledgments

* []()
* []()
* []()-->

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/cargonvis/cheap_flights_search.svg?style=for-the-badge
[contributors-url]: https://github.com/cargonvis/cheap_flights_search/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/cargonvis/cheap_flights_search.svg?style=for-the-badge
[forks-url]: https://github.com/cargonvis/cheap_flights_search/network/members
[stars-shield]: https://img.shields.io/github/stars/cargonvis/cheap_flights_search.svg?style=for-the-badge
[stars-url]: https://github.com/cargonvis/cheap_flights_search/stargazers
[issues-shield]: https://img.shields.io/github/issues/cargonvis/cheap_flights_search.svg?style=for-the-badge
[issues-url]: https://github.com/cargonvis/cheap_flights_search/issues
[license-shield]: https://img.shields.io/github/license/cargonvis/cheap_flights_search.svg?style=for-the-badge
[license-url]: https://github.com/cargonvis/cheap_flights_search/blob/master/LICENSE
[product-screenshot]: images/project_image.png
[Python.org]: https://img.shields.io/badge/python-blue?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/
[Json.org]: https://img.shields.io/badge/json-yellow?style=for-the-badge&logo=json&logoColor=white
[Json-url]: https://www.json.org/
[Pandas.org]: https://img.shields.io/badge/Pandas-black?logo=pandas&style=for-the-badge&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[Email-shield]: https://img.shields.io/badge/gmail-red?style=for-the-badge&logo=gmail&logoColor=white
[Email-url]: mailto:cgonv1993@gmail.com
[linkedin-shield]: https://img.shields.io/badge/linkedin-blue?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://linkedin.com/in/carlosgonzalezvisiedo
[Discord-shield]: https://img.shields.io/badge/discord-darkblue?style=for-the-badge&logo=discord&logoColor=white
[Discord-url]: https://discordapp.com/users/439897699299491850