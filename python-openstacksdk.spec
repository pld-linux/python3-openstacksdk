#
# Conditional build:
%bcond_with	doc	# build doc (missing dep)
%bcond_with	tests	# do perform "make test" (broken)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	An SDK for building applications to work with OpenStack
Name:		python-openstacksdk
Version:	0.9.17
Release:	8
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/o/openstacksdk/openstacksdk-%{version}.tar.gz
# Source0-md5:	0cd20ab358fd7bc89b874525c58335e2
URL:		https://pypi.python.org/pypi/openstacksdk/0.9.17
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%endif
Requires:	python-deprecation >= 1.0
Requires:	python-jsonpatch >= 1.1
Requires:	python-keystoneauth1 >= 2.21.0
Requires:	python-pbr >= 2.0.0
Requires:	python-six >= 1.9.0
Requires:	python-stevedore >= 1.20.0
Requires:	python-os-client-config >= 1.27.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The python-openstacksdk is a collection of libraries for building
applications to work with OpenStack clouds. The project aims to
provide a consistent and complete set of interactions with OpenStack's
many services, along with complete documentation, examples, and tools.

%package -n python3-openstacksdk
Summary:	An SDK for building applications to work with OpenStack
Group:		Libraries/Python
Requires:	python3-deprecation >= 1.0
Requires:	python3-jsonpatch >= 1.1
Requires:	python3-keystoneauth1 >= 2.21.0
Requires:	python3-modules
Requires:	python3-pbr >= 2.0.0
Requires:	python3-six >= 1.9.0
Requires:	python3-stevedore >= 1.20.0
Requires:	python3-os-client-config >= 1.27.0

%description -n python3-openstacksdk
The python-openstacksdk is a collection of libraries for building
applications to work with OpenStack clouds. The project aims to
provide a consistent and complete set of interactions with OpenStack's
many services, along with complete documentation, examples, and tools.

%package apidocs
Summary:	API documentation for Python openstacksdk module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona openstacksdk
Group:		Documentation

%description apidocs
API documentation for Pythona openstacksdk module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona openstacksdk.

%prep
%setup -q -n openstacksdk-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd doc
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

# when files are installed in other way that standard 'setup.py
# they need to be (re-)compiled
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

# in case there are examples provided
%if %{with python2}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python-openstacksdk-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python-openstacksdk-%{version}
find $RPM_BUILD_ROOT%{_examplesdir}/python-openstacksdk-%{version} -name '*.py' \
	| xargs sed -i '1s|^#!.*python\b|#!%{__python}|'
%endif
%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-openstacksdk-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-openstacksdk-%{version}
find $RPM_BUILD_ROOT%{_examplesdir}/python3-openstacksdk-%{version} -name '*.py' \
	| xargs sed -i '1s|^#!.*python\b|#!%{__python3}|'
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/openstack
%{py_sitescriptdir}/openstacksdk-%{version}-py*.egg-info
%{_examplesdir}/python-openstacksdk-%{version}
%endif

%if %{with python3}
%files -n python3-openstacksdk
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/openstack
%{py3_sitescriptdir}/openstacksdk-%{version}-py*.egg-info
%{_examplesdir}/python3-openstacksdk-%{version}
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/*
%endif
