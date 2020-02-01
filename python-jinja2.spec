%define tarname Jinja2
%define fname   jinja2

# jinja requires itself ( as python-sphinx use it ) to build doc
%bcond_with doc

Summary:	Python template engine
Name:		python-jinja2
Version:	2.11.1
Release:	1
License:	BSD
Group:		Development/Python
Url:		http://jinja.pocoo.org/
Source0:	https://github.com/pallets/jinja/archive/%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python2)
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
BuildRequires:	python3-distribute
BuildRequires:	python-markupsafe
%if %{with doc}
BuildRequires:	python-sphinx
%endif
Requires:	python >= 3.0
Obsoletes:	python-jinja
Suggests:	python-markupsafe
%rename python3-jinja2

%description
Jinja2 is a library for Python 2.4 and onwards that is designed to be
flexible, fast and secure. If you have any exposure to other
text-based template languages, such as Smarty or Django, you should
feel right at home with Jinja2. It's both designer and developer
friendly by sticking to Python's principles and adding functionality
useful for templating environments.

%package -n python2-jinja2
Summary:	Python template engine
Group:		Development/Python
Requires:	python2 >= 2.4
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-markupsafe
BuildRequires:	python2-distribute
 
%description -n python2-jinja2
Jinja2 is a library for Python 2.4 and onwards that is designed to be
flexible, fast and secure. If you have any exposure to other
text-based template languages, such as Smarty or Django, you should
feel right at home with Jinja2. It's both designer and developer
friendly by sticking to Python's principles and adding functionality
useful for templating environments.

%prep
%setup -q -c

mv jinja-%{version} python2
cp -r python2 python3

%build
%setup_compile_flags
cd python2
PYTHONDONTWRITEBYTECODE=  python2 setup.py build
%if %{with doc}
%make_build -C docs html
%endif
cd -

cd python3
PYTHONDONTWRITEBYTECODE=  python3 setup.py build
%if %{with doc}
%make_build -C docs html
%endif
cd -

%if 0
# Broken in 2.8
%check
cd python2
make test
cd -

cd python3
make test
cd -
%endif

%install
cd python2
python2 setup.py install --root=%{buildroot}
cd -

cd python3
python setup.py install --root=%{buildroot}
cd -

%files -n python-jinja2
%doc python2/examples
%{py_puresitedir}/%{fname}/*
%{py_puresitedir}/%{tarname}-%{version}-py%{py_ver}.egg-info
%if %{with doc}
%doc python3/docs/_build/html
%endif

%files -n python2-jinja2
%doc python2/examples
%{py2_puresitedir}/%{fname}/*
%{py2_puresitedir}/%{tarname}-%{version}-py%{py2_ver}.egg-info
%if %{with doc}
%doc python2/docs/_build/html
%endif
