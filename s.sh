#!/bin/bash
virtualenv venv
activate() {
    . ./venv/bin/activate
}
activate

#add colors to the prompt, green, blue, and red
red=`tput setaf 1`
green=`tput setaf 2`
blue=`tput setaf 4`
magenta=`tput setaf 5`
cyan=`tput setaf 6`
reset= `tput sgr0`
curl https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore > .gitignore
pip install django
echo "${green}Installing Django${reset}"
echo "${blue}Enter a Project name${reset}"
read project_name
echo "${cyan}Creating Django project${reset}"
django-admin startproject $project_name .
echo "Project created"
echo "${green}Creating a new Django app,Enter an app name${reset}"
read app_name
python manage.py startapp $app_name
echo "${magenta}Creating a new Django app${reset}"

#add app to settings.py in green 
echo "${green}Adding app to settings.py${reset}"
sed -i "/'django.contrib.staticfiles',/a\    '$app_name'," $project_name/settings.py

echo "${magenta}App added to settings.py${reset}"
echo "Creating a new template....."
mkdir $app_name/templates
echo "Hello world" > $app_name/templates/index.html


echo "${blue}Template created${reset}"
echo "Creating a new view in the app to display the template"
touch $app_name/views.py
echo "from django.shortcuts import render" >> $app_name/views.py
echo "def index(request):" >> $app_name/views.py
echo "    return render(request, 'index.html')" >> $app_name/views.py
echo "${green}View created${reset}"
#add app to urls.py
echo "${green}Adding app to urls.py......${reset}"
touch $app_name/urls.py
echo "from django.urls import path" >> $app_name/urls.py
echo "from $app_name import views" >> $app_name/urls.py
echo "urlpatterns = [path('', views.index, name='index')]" >> $app_name/urls.py
echo "${blue}App added to urls.py${reset}"

#add include to project urls.py
echo "${green}Adding app to project urls.py......${reset}"
sed -i 's/from django.urls import path/&,include/g' $project_name/urls.py

#add app to project urls.py
echo "${green}Adding app to project urls.py......${reset}"
awk '/urls),/{print;print "    path('\'''\'', include('\'''$app_name''.urls''\'')),";next}1' $project_name/urls.py > $project_name/urls.py.tmp && mv $project_name/urls.py.tmp $project_name/urls.py
sed -i "/path('admin/', admin.site.urls),/a\    path('$app_name/', include('$app_name.urls'))," $project_name/urls.py
python manage.py migrate
echo "${red}F${green}I${blue}N${magenta}I${red}S${green}H${blue}E${magenta}D ${blue}S${green}E${blue}T${magenta}U${blue}P🎉🎉${reset}"
tput init
