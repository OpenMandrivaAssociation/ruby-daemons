%define	oname	daemons

Summary:	A toolkit to create and control daemons in different ways
Name:		ruby-%{oname}
Version:	1.1.0
Release:	%mkrel 1
License:	BSD and Ruby
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
BuildArch:	noarch

%description
Daemons provides an easy way to wrap existing ruby scripts (for example a
self-written server)  to be run as a daemon and to be controlled by simple
start/stop/restart commands.  You can also call blocks as daemons and control
them from the parent or just daemonize the current process.  Besides this basic
functionality, daemons offers many advanced features like exception backtracing
and logging (in case your ruby script crashes) and monitoring and automatic
restarting of your processes if they crash.

%prep

%build

%install
rm -rf %{buildroot}
gem install --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}
rm -rf %{buildroot}%{ruby_gemdir}/{cache,gems/%{oname}-%{version}/ext}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
