# Orion

## Team Members (Github usernames):

- Jamie Mei (Meij03)
- Amadou Oury Diallo (fdnthecoder)
- Weixiong Zhu (itsweiwei)
- Momin Qadri (mominqadri)

## Backend website

To see all APIs, please refer to this link

`https://orion-crepe.herokuapp.com/`

## Description:

Current job searching for college students have been very unorganized and students have struggled in organizing the number of companies they applied for and their applications. Our project Orion is intended to help college students in organizing their internship/job application searching opportunies. As well as creating a community space for fellow students to post internship or event opportunities.
 
## Setup
 
To configure your system for development, first install Python 3 and git and
then run
`make dev_env` (on Linux).

In order to build production, in the top level directory, run:

`make prod`
Follow the outputted instructions for setting your environment variables.
In order to run tests before run
`make tests`

## Basic functionalities
- Must be able to access user profile
- Must be able to add job posting and add job posting to appication tracker

## Requirements

Users should be able to:

1. Add/Move applications on our Kanban Board
   - Add Applications to Tracker
      - Manually adding application information on to card
      - Adding through job post clicks
   - Movie/Update Application
      - Manual move between different sections
   - Delete (or Archives) Applications
      - Delete or move archives
1. Post applications on community board/home
   - Post applications
   - Connection between post to kanban board - in a default section(wishlist/bucketlist)

API should be able to:

1. User login
   1. User logout
   1. User sign up
2. Add Job Posting
   1. Delete Job posting
   1. Edit Job posting
3. Add Job posting to application tracker (Kanban board)
   1. Updates location of card based of user movement of card

The requirements for a design project include:

1. Everything under source code control
1. Documentation integrated with code.
1. Project build automated.
1. Automated testing in place.
1. Automated code checking in place.
1. Test code coverage measured.
1. Automated deployment to production

## Design

The following is a standard toolkit for this course. You _may_ use other tools,
but our ability to help you master them will not be as high as with the
standard tools.

1. Use `git`
1. Use `pydoc`
1. Use `make`
1. Use `unittest`
1. Use `flake8`
1. Use `coverage`
1. Use `Travis`