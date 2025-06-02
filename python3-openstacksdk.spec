#
# Conditional build:
%bcond_without	doc	# build doc (missing dep)
%bcond_with	tests	# unit tests (incomplete dependencies)

Summary:	An SDK for building applications to work with OpenStack
Summary(pl.UTF-8):	SDK do budowania aplikacji działających z OpenStack
Name:		python3-openstacksdk
Version:	4.5.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/o/openstacksdk/openstacksdk-%{version}.tar.gz
# Source0-md5:	7cb87c680113f4b25f47a086a9b9571e
URL:		https://pypi.org/project/openstacksdk/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
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
Requires:	python3-modules >= 1:3.9
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
%py3_build %{?with_tests:test}

%if %{with doc}
sphinx-build-3 -b html doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/openstack/tests

%{__mv} $RPM_BUILD_ROOT%{_bindir}/openstack-inventory{,-3}
ln -sf openstack-inventory-3 $RPM_BUILD_ROOT%{_bindir}/openstack-inventory

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-openstacksdk-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-openstacksdk-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%attr(755,root,root) %{_bindir}/openstack-inventory
%attr(755,root,root) %{_bindir}/openstack-inventory-3
%{py3_sitescriptdir}/openstack
%{py3_sitescriptdir}/openstacksdk-%{version}-py*.egg-info
%{_examplesdir}/python3-openstacksdk-%{version}

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,contributor,install,user,*.html,*.js}
%endif
