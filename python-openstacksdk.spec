#
# Conditional build:
%bcond_without	doc	# build doc (missing dep)
%bcond_with	tests	# unit tests (incomplete dependencies)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	An SDK for building applications to work with OpenStack
Summary(pl.UTF-8):	SDK do budowania aplikacji działających z OpenStack
Name:		python-openstacksdk
# keep 0.39.x here for python2 support
Version:	0.39.0
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/o/openstacksdk/openstacksdk-%{version}.tar.gz
# Source0-md5:	7398126a03a068b94f2207fa714b47c4
Patch0:		openstacksdk-collections.patch
URL:		https://pypi.org/project/openstacksdk/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr >= 3.0.0
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-PyYAML >= 3.12
BuildRequires:	python-appdirs >= 1.3.0
BuildRequires:	python-cryptography >= 2.1
BuildRequires:	python-ddt >= 1.0.1
BuildRequires:	python-decorator >= 3.4.0
BuildRequires:	python-dogpile.cache >= 0.6.5
BuildRequires:	python-extras >= 1.0.0
BuildRequires:	python-fixtures >= 3.0.0
BuildRequires:	python-futures >= 3.0.0
BuildRequires:	python-ipaddress >= 1.0.17
BuildRequires:	python-iso8601 >= 0.1.11
BuildRequires:	python-jmespath >= 0.9.0
BuildRequires:	python-jsonpatch >= 1.21
BuildRequires:	python-jsonschema >= 2.0.0
BuildRequires:	python-keystoneauth1 >= 3.18.0
BuildRequires:	python-munch >= 2.1.0
BuildRequires:	python-netifaces >= 0.10.4
BuildRequires:	python-os-service-types >= 1.7.0
BuildRequires:	python-oslo.config >= 6.1.0
BuildRequires:	python-oslotest >= 3.2.0
BuildRequires:	python-prometheus-client >= 0.4.2
BuildRequires:	python-requests-mock >= 1.2.0
BuildRequires:	python-requestsexceptions >= 1.2.0
BuildRequires:	python-six >= 1.10.0
BuildRequires:	python-statsd >= 3.3.0
BuildRequires:	python-stestr >= 1.0.0
BuildRequires:	python-subunit >= 1.0.0
BuildRequires:	python-testrepository >= 0.0.18
BuildRequires:	python-testscenarios >= 0.4
BuildRequires:	python-testtools >= 2.2.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-pbr >= 3.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-PyYAML >= 3.12
BuildRequires:	python3-appdirs >= 1.3.0
BuildRequires:	python3-cryptography >= 2.1
BuildRequires:	python3-ddt >= 1.0.1
BuildRequires:	python3-decorator >= 3.4.0
BuildRequires:	python3-dogpile.cache >= 0.6.5
BuildRequires:	python3-extras >= 1.0.0
BuildRequires:	python3-fixtures >= 3.0.0
BuildRequires:	python3-iso8601 >= 0.1.11
BuildRequires:	python3-jmespath >= 0.9.0
BuildRequires:	python3-jsonpatch >= 1.21
BuildRequires:	python3-jsonschema >= 2.0.0
BuildRequires:	python3-keystoneauth1 >= 3.18.0
BuildRequires:	python3-munch >= 2.1.0
BuildRequires:	python3-netifaces >= 0.10.4
BuildRequires:	python3-os-service-types >= 1.7.0
BuildRequires:	python3-oslo.config >= 6.1.0
BuildRequires:	python3-oslotest >= 3.2.0
BuildRequires:	python3-prometheus-client >= 0.4.2
BuildRequires:	python3-requests-mock >= 1.2.0
BuildRequires:	python3-requestsexceptions >= 1.2.0
BuildRequires:	python3-six >= 1.10.0
BuildRequires:	python3-statsd >= 3.3.0
BuildRequires:	python3-stestr >= 1.0.0
BuildRequires:	python3-subunit >= 1.0.0
BuildRequires:	python3-testrepository >= 0.0.18
BuildRequires:	python3-testscenarios >= 0.4
BuildRequires:	python3-testtools >= 2.2.0
%endif
%endif
%if %{with doc}
BuildRequires:	python3-bs4 >= 4.6.0
BuildRequires:	python3-docutils >= 0.11
BuildRequires:	python3-dogpile.cache >= 0.6.5
BuildRequires:	python3-jsonpatch >= 1.21
BuildRequires:	python3-keystoneauth1 >= 3.18.0
BuildRequires:	python3-munch >= 2.1.0
BuildRequires:	python3-netifaces >= 0.10.4
BuildRequires:	python3-openstackdocstheme >= 1.20.0
BuildRequires:	python3-reno >= 2.5.0
BuildRequires:	python3-requestsexceptions >= 1.2.0
BuildRequires:	python3-sphinxcontrib-svg2pdfconverter >= 0.1.0
BuildRequires:	sphinx-pdg-3 >= 2.1.1
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python openstacksdk package is a collection of libraries for building
applications to work with OpenStack clouds. The project aims to
provide a consistent and complete set of interactions with OpenStack's
many services, along with complete documentation, examples, and tools.

%description -l pl.UTF-8
Pakiet Pythona openstacksdk to zbiór bibliotek do budowania aplikacji
działających z chmurami OpenStack. Celem projektu jest zapewnienie
spójnego i kompletnego zbioru interakcji z wieloma usługami OpenStack
wraz z pełną dokumentacją, przykładami i narzędziami.

%package -n python3-openstacksdk
Summary:	An SDK for building applications to work with OpenStack
Summary(pl.UTF-8):	SDK do budowania aplikacji działających z OpenStack
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-openstacksdk
Python openstacksdk package is a collection of libraries for building
applications to work with OpenStack clouds. The project aims to
provide a consistent and complete set of interactions with OpenStack's
many services, along with complete documentation, examples, and tools.

%description -n python3-openstacksdk -l pl.UTF-8
Pakiet Pythona openstacksdk to zbiór bibliotek do budowania aplikacji
działających z chmurami OpenStack. Celem projektu jest zapewnienie
spójnego i kompletnego zbioru interakcji z wieloma usługami OpenStack
wraz z pełną dokumentacją, przykładami i narzędziami.

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
%patch -P 0 -p1

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
sphinx-build-3 -b html doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/openstack/tests

%{__mv} $RPM_BUILD_ROOT%{_bindir}/openstack-inventory{,-2}
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/openstack/tests

%{__mv} $RPM_BUILD_ROOT%{_bindir}/openstack-inventory{,-3}
ln -sf openstack-inventory-3 $RPM_BUILD_ROOT%{_bindir}/openstack-inventory
%endif

%if %{with python2}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python-openstacksdk-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python-openstacksdk-%{version}
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-openstacksdk-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-openstacksdk-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%attr(755,root,root) %{_bindir}/openstack-inventory-2
%{py_sitescriptdir}/openstack
%{py_sitescriptdir}/openstacksdk-%{version}-py*.egg-info
%{_examplesdir}/python-openstacksdk-%{version}
%endif

%if %{with python3}
%files -n python3-openstacksdk
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%attr(755,root,root) %{_bindir}/openstack-inventory
%attr(755,root,root) %{_bindir}/openstack-inventory-3
%{py3_sitescriptdir}/openstack
%{py3_sitescriptdir}/openstacksdk-%{version}-py*.egg-info
%{_examplesdir}/python3-openstacksdk-%{version}
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,contributor,install,user,*.html,*.js}
%endif
