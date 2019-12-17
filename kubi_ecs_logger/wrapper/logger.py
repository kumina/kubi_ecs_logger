"""
Logger is a wrapper around ECS-based logging models.
This class is initiated only ones and keeps the defaults and state.
When the class is called the base is reinitialized.
Also sending out the log will reinitialize the base.

Creating a log line:
Logger(message="This is my log message.").event(action="logging").out(severity='debug')

The first field object added since initialization of a specific type will be inserted,
the following field object of the same time will be neglected.
"""
import sys
from typing import Optional, List, Union
from datetime import datetime

from kubi_ecs_logger.models.fields import *

from kubi_ecs_logger.utils import pprint
from kubi_ecs_logger.models import Base, BaseSchema, Severity


class Logger:
    __instance: 'Logger' = None
    _defaults: dict = {}
    _base: Base = None
    _dev: bool = False
    _severity_output_level: Severity = Severity.INFO

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Logger, cls).__new__(cls)
        cls.__instance.base()
        return cls.__instance

    @property
    def dev(self):
        return self._dev

    @dev.setter
    def dev(self, value):
        assert isinstance(value, bool)  # Check
        self._dev = value

    @property
    def severity_output_level(self):
        return self._severity_output_level

    @severity_output_level.setter
    def severity_output_level(self, value):
        assert isinstance(value, Severity)  # Check
        self._severity_output_level = value

    @property
    def defaults(self):
        return self._defaults

    @defaults.setter
    def defaults(self, value):
        assert isinstance(value, dict)  # Check
        self._defaults = value

    def base(self, date: datetime = None, labels: dict = None, message: str = None,
             tags: List[str] = None, **kwargs) -> 'Logger':
        defaults = self.__get_defaults_for(Base)
        if defaults:
            kwargs.update(defaults)

        self._base = Base(date=date, labels=labels, message=message, tags=tags, **kwargs)
        return self

    def agent(self, ephemeral_id: str = None, id: str = None, name: str = None,
              type: str = None, version: str = None, **kwargs):
        defaults = self.__get_defaults_for(Agent)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Agent(ephemeral_id=ephemeral_id, id=id, name=name, type=type, version=version, **kwargs))
        return self

    def client(self, address: str = None, bytes: int = None, domain: str = None, ip: str = None,
               mac: str = None, packets: int = None, port: int = None, **kwargs):
        defaults = self.__get_defaults_for(Client)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Client(address=address, bytes=bytes, domain=domain, ip=ip, mac=mac, packets=packets,
                                     port=port, **kwargs))
        return self

    def cloud(self, account_id: str = None, availability_zone: str = None, instance_id: str = None,
              instance_name: str = None, machine_type: str = None, provider: str = None,
              region: str = None, **kwargs):
        defaults = self.__get_defaults_for(Cloud)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Cloud(account_id=account_id, availability_zone=availability_zone, instance_id=instance_id,
                                    instance_name=instance_name, machine_type=machine_type, provider=provider,
                                    region=region, **kwargs))
        return self

    def container(self, id: str = None, image_name: str = None, image_tag: str = None,
                  labels: dict = None, name: str = None, runtime: str = None, **kwargs):
        defaults = self.__get_defaults_for(Container)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Container(id=id, image_name=image_name, image_tag=image_tag, labels=labels,
                                        name=name, runtime=runtime, **kwargs))
        return self

    def destination(self, address: str = None, bytes: int = None, domain: str = None, ip: str = None,
                    mac: str = None, packets: int = None, port: int = None, **kwargs):
        defaults = self.__get_defaults_for(Destination)
        if defaults:
            kwargs.update(defaults)
        self._base.add_object(Destination(address=address, bytes=bytes, domain=domain, ip=ip, mac=mac, packets=packets,
                                          port=port, **kwargs))
        return self

    def ecs(self, version: str = None, **kwargs):
        defaults = self.__get_defaults_for(Client)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(ECS(version=version))
        return self

    def error(self, code: str = None, id: str = None, message: str = None, **kwargs) -> 'Logger':
        defaults = self.__get_defaults_for(Error)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Error(code=code, id=id, message=message, **kwargs))
        return self

    def event(self, action: str = None, category: str = None, created: datetime = None,
              dataset: str = None, risk_score: float = None, severity: int = None,
              **kwargs) -> 'Logger':
        defaults = self.__get_defaults_for(Event)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Event(action=action, category=category, created=created, dataset=dataset,
                                    risk_score=risk_score, severity=severity, **kwargs))
        return self

    def file(self, ctime: datetime = None, device: str = None, extension: str = None, gid: str = None,
             group: str = None, inode: str = None, mode: str = None, mtime: datetime = None, owner: str = None,
             path: str = None, size: int = None, target_path: str = None, type: str = None, uid: str = None,
             **kwargs):
        defaults = self.__get_defaults_for(File)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(File(ctime=ctime, device=device, extension=extension, gid=gid, group=group,
                                   inode=inode, mode=mode, mtime=mtime, owner=owner, path=path, size=size,
                                   target_path=target_path, type=type, uid=uid, **kwargs))
        return self

    def geo(self, city_name: str = None, continent_name: str = None, country_iso_code: str = None,
            country_name: str = None, location: dict = None, name: str = None, region_iso_code: str = None,
            region_name: str = None, **kwargs):
        defaults = self.__get_defaults_for(Geo)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Geo(city_name=city_name, continent_name=continent_name, country_iso_code=country_iso_code,
                                  country_name=country_name, location=location, name=name,
                                  region_iso_code=region_iso_code,
                                  region_name=region_name, **kwargs))
        return self

    def group(self, id: str = None, name: str = None, **kwargs):
        defaults = self.__get_defaults_for(Group)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Group(id=id, name=name, **kwargs))
        return self

    def host(self, architecture: str = None, hostname: str = None, id: str = None, ip: str = None,
             mac: str = None, name: str = None, type: str = None, **kwargs):
        defaults = self.__get_defaults_for(Host)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Host(architecture=architecture, hostname=hostname, id=id, ip=ip, mac=mac,
                                   name=name, type=type, **kwargs))
        return self

    def http_request(self, body_bytes: int = None, body_content: str = None, bytes: int = None, method: str = None,
                     referrer: str = None, version: str = None, **kwargs):
        defaults = self.__get_defaults_for(HttpRequest)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(HttpRequest(body_bytes=body_bytes, body_content=body_content, bytes=bytes, method=method,
                                          referrer=referrer, version=version, **kwargs))
        return self

    def http_response(self, body_bytes: int = None, body_content: str = None, bytes: int = None,
                      status_code: str = None, version: str = None, **kwargs):
        defaults = self.__get_defaults_for(HttpResponse)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(HttpResponse(body_bytes=body_bytes, body_content=body_content, bytes=bytes,
                                           status_code=status_code, version=version, **kwargs))
        return self

    def log(self, level: Union[str, Severity] = None, original: str = None, **kwargs) -> 'Logger':
        defaults = self.__get_defaults_for(LogLine)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(LogLine(level=level, original=original, **kwargs))
        return self

    def network(self, application: str = None, bytes: int = None, community_id: str = None, direction: str = None,
                forwarded_ip: str = None, iana_number: str = None, name: str = None, packets: int = None,
                protocol: str = None, transport: str = None, type: str = None, **kwargs):
        defaults = self.__get_defaults_for(Network)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Network(application=application, bytes=bytes, community_id=community_id,
                                      direction=direction, forwarded_ip=forwarded_ip, iana_number=iana_number,
                                      name=name, packets=packets, protocol=protocol, transport=transport, type=type,
                                      **kwargs))
        return self

    def observer(self, hostname: str = None, ip: str = None, mac: str = None, serial_number: str = None,
                 type: str = None, vendor: str = None, version: str = None, **kwargs):
        defaults = self.__get_defaults_for(Observer)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Observer(hostname=hostname, ip=ip, mac=mac, serial_number=serial_number, type=type,
                                       vendor=vendor, version=version, **kwargs))
        return self

    def organization(self, id: str = None, name: str = None, **kwargs):
        defaults = self.__get_defaults_for(Organization)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Organization(id=id, name=name, **kwargs))
        return self

    def os(self, family: str = None, full: str = None, kernel: str = None, name: str = None, platform: str = None,
           version: str = None, **kwargs):
        defaults = self.__get_defaults_for(OS)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(OS(family=family, full=full, kernel=kernel, name=name, platform=platform, version=version,
                                 **kwargs))
        return self

    def process(self, args: List[str] = None, executable: str = None, name: str = None, pid: int = None,
                ppid: int = None, start: datetime = None, thread_id: int = None, title: str = None,
                working_directory: str = None, **kwargs):
        defaults = self.__get_defaults_for(Process)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Process(args=args, executable=executable, name=name, pid=pid, ppid=ppid, start=start,
                                      thread_id=thread_id, title=title, working_directory=working_directory, **kwargs))
        return self

    def related(self, ip: str = None, **kwargs):
        defaults = self.__get_defaults_for(Related)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Related(ip=ip, **kwargs))
        return self

    def server(self, address: str = None, bytes: int = None, domain: str = None, ip: str = None, mac: str = None,
               packets: int = None, port: int = None, **kwargs):
        defaults = self.__get_defaults_for(Server)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Server(address=address, bytes=bytes, domain=domain, ip=ip, mac=mac, packets=packets,
                                     port=port, **kwargs))
        return self

    def service(self, ephemeral_id: str = None, id: str = None, name: str = None, state: str = None, type: str = None,
                version: str = None, **kwargs):
        defaults = self.__get_defaults_for(Service)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Service(ephemeral_id=ephemeral_id, id=id, name=name, state=state, type=type,
                                      version=version, **kwargs))
        return self

    def source(self, address: str = None, bytes: int = None, domain: str = None, ip: str = None, mac: str = None,
               packets: int = None, port: int = None, **kwargs):
        defaults = self.__get_defaults_for(Source)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Source(address=address, bytes=bytes, domain=domain, ip=ip, mac=mac, packets=packets,
                                     port=port, **kwargs))
        return self

    def url(self, domain: str = None, fragment: str = None, full: str = None, original: str = None,
            password: str = None, path: str = None, port: int = None, query: str = None, scheme: str = None,
            username: str = None, **kwargs):
        defaults = self.__get_defaults_for(Url)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(Url(domain=domain, fragment=fragment, full=full, original=original, password=password,
                                  path=path, port=port, query=query, scheme=scheme, username=username, **kwargs))
        return self

    def user(self, email: str = None, full_name: str = None, hash: str = None, id: str = None, name: str = None,
             **kwargs):
        defaults = self.__get_defaults_for(User)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(User(email=email, full_name=full_name, hash=hash, id=id, name=name, **kwargs))
        return self

    def user_agent(self, device_name: str = None, name: str = None, original: str = None, version: str = None,
                   **kwargs):
        defaults = self.__get_defaults_for(UserAgent)
        if defaults:
            kwargs.update(defaults)

        self._base.add_object(UserAgent(device_name=device_name, name=name, original=original, version=version,
                                        **kwargs))
        return self

    def out(self, severity: Severity = Severity.DEBUG):
        assert isinstance(severity, Severity)

        self.__append_log_level(severity)

        if severity >= self._severity_output_level:
            self.__output()

        # Reset
        self.base()

    def __get_defaults_for(self, obj: type) -> Optional[dict]:
        name = str(obj.__name__).lower()
        if name in self._defaults:
            return self._defaults[name]
        return None

    def __output(self):
        """
        The internal function that handles/passes on the printing
        """
        if self._dev:
            pprint(BaseSchema().dump(self._base).data, output_destination=sys.stdout)
        else:
            print(BaseSchema().dumps(self._base).data, file=sys.stdout)

    def __append_log_level(self, severity_level: Severity):
        # Append log level if doesn't exist
        if hasattr(self._base, "logline"):
            if self._base.logline.level is None:
                self._base.logline.level = severity_level
            else:
                return

        self._base.add_object(LogLine(level=severity_level))
