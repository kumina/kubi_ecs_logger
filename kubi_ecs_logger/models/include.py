from marshmallow import fields

from .fields import *

INCLUDE_FIELDS = {
    'agent': fields.Nested(AgentSchema),
    'client': fields.Nested(ClientSchema),
    'cloud': fields.Nested(CloudSchema),
    'container': fields.Nested(ContainerSchema),
    'destination': fields.Nested(DestinationSchema),
    'ecs': fields.Nested(ECSSchema),
    'error': fields.Nested(ErrorSchema),
    'event': fields.Nested(EventSchema),
    'file': fields.Nested(FileSchema),
    'geo': fields.Nested(GeoSchema),
    'group': fields.Nested(GroupSchema),
    'host': fields.Nested(HostSchema),
    'httprequest': fields.Nested(HttpRequestSchema),
    'httpresponse': fields.Nested(HttpResponseSchema),
    'logline': fields.Nested(LogLineSchema),
    'network': fields.Nested(NetworkSchema),
    'observer': fields.Nested(ObserverSchema),
    'organization': fields.Nested(OrganizationSchema),
    'os': fields.Nested(OSSchema),
    'process': fields.Nested(ProcessSchema),
    'related': fields.Nested(RelatedSchema),
    'server': fields.Nested(ServerSchema),
    'service': fields.Nested(ServiceSchema),
    'source': fields.Nested(SourceSchema),
    'url': fields.Nested(UrlSchema),
    'user': fields.Nested(UserSchema),
    'useragent': fields.Nested(UserAgentSchema),
}
