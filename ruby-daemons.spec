%define	oname	daemons

Summary:	A toolkit to create and control daemons in different ways
Name:		ruby-%{oname}
Version:	1.1.6
Release:	3
License:	BSD and Ruby
Group:		Development/Ruby
URL:		https://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
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
gem install --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}
rm -rf %{buildroot}%{ruby_gemdir}/{cache,gems/%{oname}-%{version}/ext}

%files
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.6-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Fri Jan 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.6-1
+ Revision: 769368
- version update 1.1.6

* Sat Sep 18 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 579409
- new release: 1.1.0
- don't install gem archive
- remove manual ruby dependency

* Tue Feb 02 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0.10-1mdv2010.1
+ Revision: 499399
- import ruby-daemons


* Mon Feb  1 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0.10
- initial release
