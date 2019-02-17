{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf200
{\fonttbl\f0\fnil\fcharset0 HelveticaNeue-Bold;\f1\fnil\fcharset0 HelveticaNeue;\f2\fnil\fcharset0 Menlo-Regular;
}
{\colortbl;\red255\green255\blue255;\red27\green31\blue34;\red255\green255\blue255;\red10\green77\blue204;
\red21\green23\blue26;\red252\green39\blue18;\red255\green255\blue255;\red217\green11\blue5;\red244\green246\blue249;
}
{\*\expandedcolortbl;;\cssrgb\c14118\c16078\c18039;\cssrgb\c100000\c100000\c100000;\cssrgb\c1176\c40000\c83922;
\cssrgb\c10588\c12157\c13725\c4706;\cssrgb\c100000\c25271\c7591;\csgray\c100000;\cssrgb\c88946\c14202\c0;\cssrgb\c96471\c97255\c98039;
}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}.}{\leveltext\leveltemplateid1\'02\'00.;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid1}
{\list\listtemplateid2\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}.}{\leveltext\leveltemplateid101\'02\'00.;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid2}
{\list\listtemplateid3\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}.}{\leveltext\leveltemplateid201\'02\'00.;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid3}
{\list\listtemplateid4\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}.}{\leveltext\leveltemplateid301\'02\'00.;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid4}
{\list\listtemplateid5\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}.}{\leveltext\leveltemplateid401\'02\'00.;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid5}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}{\listoverride\listid2\listoverridecount0\ls2}{\listoverride\listid3\listoverridecount0\ls3}{\listoverride\listid4\listoverridecount0\ls4}{\listoverride\listid5\listoverridecount0\ls5}}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\hyphauto1\hyphfactor90
\deftab720
\pard\pardeftab720\sl600\sa320\partightenfactor0

\f0\b\fs48 \cf2 \cb3 \expnd0\expndtw0\kerning0
Log Analysis Project 
\fs36 \cf4 \cb1 \
\pard\pardeftab720\sl440\sa320\partightenfactor0
\cf2 \cb3 Project Description:\
\pard\pardeftab720\sl360\sa320\partightenfactor0

\f1\b0\fs32 \cf2 Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.\
\pard\pardeftab720\sl300\partightenfactor0

\f0\b\fs30 \cf4 \cb1 \
\pard\pardeftab720\sl360\sa320\partightenfactor0
\cf2 \cb3 Questions to Answer:\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl360\partightenfactor0
\ls1\ilvl0
\fs32 \cf2 \kerning1\expnd0\expndtw0 {\listtext	1.	}\expnd0\expndtw0\kerning0
What are the most popular three articles of all time?
\f1\b0 \'a0Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.\cb1 \
\ls1\ilvl0
\f0\b \cb3 \kerning1\expnd0\expndtw0 {\listtext	2.	}\expnd0\expndtw0\kerning0
Who are the most popular article authors of all time?
\f1\b0 \'a0That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.\cb1 \
\ls1\ilvl0
\f0\b \cb3 \kerning1\expnd0\expndtw0 {\listtext	3.	}\expnd0\expndtw0\kerning0
On which days did more than 1% of requests lead to errors?
\f1\b0 \'a0The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.\cb1 \
\pard\pardeftab720\sl360\partightenfactor0

\f0\b\fs36 \cf4 \
\pard\pardeftab720\sl440\sa320\partightenfactor0
\cf2 \cb3 This Project Requires a Bit of Setup:\
\pard\pardeftab720\sl360\sa320\partightenfactor0

\f1\b0\fs32 \cf2 This project is run in a virutal machine created using Vagrant so there are a few steps to get set up:\
\pard\pardeftab720\sl320\partightenfactor0

\f0\b \cf4 \cb1 \
\pard\pardeftab720\sl400\sa320\partightenfactor0
\cf2 \cb3 Installing the dependencies and setting up the files:\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl360\partightenfactor0
\ls2\ilvl0
\f1\b0 \cf2 \kerning1\expnd0\expndtw0 {\listtext	1.	}\expnd0\expndtw0\kerning0
Install\'a0{\field{\*\fldinst{HYPERLINK "https://www.vagrantup.com/"}}{\fldrslt \cf4 Vagrant}}\cb1 \
\ls2\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	2.	}\expnd0\expndtw0\kerning0
Install\'a0{\field{\*\fldinst{HYPERLINK "https://www.virtualbox.org/"}}{\fldrslt \cf4 VirtualBox}}\cb1 \
\ls2\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	3.	}\expnd0\expndtw0\kerning0
Download the vagrant setup files from\'a0{\field{\*\fldinst{HYPERLINK "https://github.com/udacity/fullstack-nanodegree-vm"}}{\fldrslt \cf4 Udacity's Github}}\'a0These files configure the virtual machine and install all the tools needed to run this project.\cb1 \
\ls2\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	4.	}\expnd0\expndtw0\kerning0
Download the database setup:\'a0{\field{\*\fldinst{HYPERLINK "https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip"}}{\fldrslt \cf4 data}}\cb1 \
\ls2\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	5.	}\expnd0\expndtw0\kerning0
Unzip the data to get the newsdata.sql file.\cb1 \
\ls2\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	6.	}\expnd0\expndtw0\kerning0
Put the newsdata.sql file into the vagrant directory\cb1 \
\ls2\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	7.	}\expnd0\expndtw0\kerning0
Download this project:\'a0{\field{\*\fldinst{HYPERLINK "https://github.com/lythro10/Udacity-Log-Analysis.git"}}{\fldrslt \cf4 log analysis}}\cb1 \
\ls2\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	8.	}\expnd0\expndtw0\kerning0
Upzip as needed and copy all files into the vagrant directory into a folder called Log-Analysis\cb1 \
\pard\pardeftab720\sl320\partightenfactor0

\f0\b \cf4 \
\pard\pardeftab720\sl400\sa320\partightenfactor0
\cf2 \cb3 Start the Virtual Machine:\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl360\partightenfactor0
\ls3\ilvl0
\f1\b0 \cf2 \kerning1\expnd0\expndtw0 {\listtext	1.	}\expnd0\expndtw0\kerning0
Open Terminal and navigate to the project folders we setup above.\cb1 \
\ls3\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	2.	}\expnd0\expndtw0\kerning0
cd into the vagrant directory\cb1 \
\ls3\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	3.	}\expnd0\expndtw0\kerning0
Run\'a0
\f2\fs27\fsmilli13600 \cb5 vagrant up
\f1\fs32 \cb3 \'a0to build the VM for the first time.\cb1 \
\ls3\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	4.	}\expnd0\expndtw0\kerning0
Once it is built, run\'a0
\f2\fs27\fsmilli13600 \cb5 vagrant ssh
\f1\fs32 \cb3 \'a0to connect.\cb1 \
\ls3\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	5.	}\expnd0\expndtw0\kerning0
cd into the correct project directory:\'a0
\f2\fs27\fsmilli13600 \cf6 \cb7 cd /vagrant/Log-Analysis
\f1\fs32 \cf2 \cb1 \
\pard\pardeftab720\sl320\partightenfactor0

\f0\b \cf4 \
\pard\pardeftab720\sl400\sa320\partightenfactor0
\cf2 \cb3 Load the data into the database:\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl360\partightenfactor0
\ls4\ilvl0
\f1\b0 \cf2 \kerning1\expnd0\expndtw0 {\listtext	1.	}\expnd0\expndtw0\kerning0
Load the data using the following command:\'a0
\f2\fs27\fsmilli13600 \cb5 psql -d news -f newsdata.sql
\f1\fs32 \cb1 \
\
\pard\pardeftab720\sl360\partightenfactor0

\f0\b\fs36 \cf4 \
\pard\pardeftab720\sl440\sa320\partightenfactor0
\cf2 \cb3 Run The Project Already!\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl360\partightenfactor0
\ls5\ilvl0
\f1\b0\fs32 \cf2 \kerning1\expnd0\expndtw0 {\listtext	1.	}\expnd0\expndtw0\kerning0
You should already have vagrant up and be connected to it.\cb1 \
\ls5\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	2.	}\expnd0\expndtw0\kerning0
If you aren't already, cd into the correct project directory:\'a0
\f2\fs27\fsmilli13600 \cf8 \cb5 cd /vagrant/Log-Analysis
\f1\fs32 \cb1 \
\ls5\ilvl0\cf2 \cb3 \kerning1\expnd0\expndtw0 {\listtext	3.	}\expnd0\expndtw0\kerning0
Run\'a0
\f2\fs27\fsmilli13600 \cf6 \cb7 python logs.py
\f1\fs32 \cf2 \cb1 \
\pard\pardeftab720\sl360\sa320\partightenfactor0
\cf2 \cb3 Generating this information will take several seconds, but will now start loading.\
\pard\pardeftab720\sl360\partightenfactor0

\f0\b\fs36 \cf4 \cb1 \
\pard\pardeftab720\sl440\sa320\partightenfactor0
\cf2 \cb3 Expected Output:\
\pard\pardeftab720\sl380\partightenfactor0

\f2\b0\fs27\fsmilli13600 \cf2 \cb9 Please wait the results are being calculated Thank you...\
\
\
What are the most popular three articles of all time?:\
(1) "Candidate is jerk, alleges rival" with 338647 views\
(2) "Bears love berries, alleges bear" with 253801 views\
(3) "Bad things gone, say good people" with 170098 views\
\
Who are the most popular article authors of all time? :\
(1) Ursula La Multa with 507594 views\
(2) Rudolf von Treppenwitz with 423457 views\
(3) Anonymous Contributor with 170098 views\
\
On which days did more than 1% of requests lead to errors? :\
July 17, 2016 -- 2.3% errors\
\
\pard\pardeftab720\sl360\partightenfactor0

\f0\b\fs36 \cf4 \cb1 \
}