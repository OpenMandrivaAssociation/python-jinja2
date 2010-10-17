%define tarname Jinja2
%define name	python-jinja2
%define version 2.5.4
%define release %mkrel 1

Summary:	Python template engine
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://jinja.pocoo.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Obsoletes:	python-jinja
Requires:	python >= 2.4
Suggests:	python-markupsafe
BuildRequires:	python-devel >= 2.4, python-setuptools
BuildRequires:	python-sphinx

%description
Jinja2 is a library for Python 2.4 and onwards that is designed to be
flexible, fast and secure. If you have any exposure to other
text-based template languages, such as Smarty or Django, you should
feel right at home with Jinja2. It's both designer and developer
friendly by sticking to Python's principles and adding functionality
useful for templating environments.

%prep
%setup -q -n %{tarname}-%{version}

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build 
%make -C docs html

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
%__rm -rf docs/_build/html/.buildinfo

%check
make test

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc AUTHORS CHANGES LICENSE examples docs/_build/html
