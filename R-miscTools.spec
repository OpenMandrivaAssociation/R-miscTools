%global packname  miscTools
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.6.16
Release:          1
Summary:          Miscellanneous Tools and Utilities
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/miscTools_0.6-16.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-Ecdat 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-Ecdat 

%description
Miscellanneous small tools and utilities

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
