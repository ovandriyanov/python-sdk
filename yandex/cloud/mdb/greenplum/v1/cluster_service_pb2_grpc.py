# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.mdb.greenplum.v1 import cluster_pb2 as yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__pb2
from yandex.cloud.mdb.greenplum.v1 import cluster_service_pb2 as yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class ClusterServiceStub(object):
    """A set of methods for managing Greenplum® clusters.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.mdb.greenplum.v1.ClusterService/Get',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.GetClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__pb2.Cluster.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.mdb.greenplum.v1.ClusterService/List',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClustersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClustersResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.mdb.greenplum.v1.ClusterService/Create',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.CreateClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.mdb.greenplum.v1.ClusterService/Update',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.UpdateClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.mdb.greenplum.v1.ClusterService/Delete',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.DeleteClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Start = channel.unary_unary(
                '/yandex.cloud.mdb.greenplum.v1.ClusterService/Start',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.StartClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Stop = channel.unary_unary(
                '/yandex.cloud.mdb.greenplum.v1.ClusterService/Stop',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.StopClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.mdb.greenplum.v1.ClusterService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterOperationsResponse.FromString,
                )
        self.ListMasterHosts = channel.unary_unary(
                '/yandex.cloud.mdb.greenplum.v1.ClusterService/ListMasterHosts',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterHostsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterHostsResponse.FromString,
                )
        self.ListSegmentHosts = channel.unary_unary(
                '/yandex.cloud.mdb.greenplum.v1.ClusterService/ListSegmentHosts',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterHostsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterHostsResponse.FromString,
                )
        self.ListLogs = channel.unary_unary(
                '/yandex.cloud.mdb.greenplum.v1.ClusterService/ListLogs',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterLogsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterLogsResponse.FromString,
                )
        self.ListBackups = channel.unary_unary(
                '/yandex.cloud.mdb.greenplum.v1.ClusterService/ListBackups',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterBackupsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterBackupsResponse.FromString,
                )
        self.Restore = channel.unary_unary(
                '/yandex.cloud.mdb.greenplum.v1.ClusterService/Restore',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.RestoreClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class ClusterServiceServicer(object):
    """A set of methods for managing Greenplum® clusters.
    """

    def Get(self, request, context):
        """Returns the specified Greenplum® cluster.

        To get the list of available Greenplum® clusters, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves a list of Greenplum® clusters that belong to the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a Greenplum® cluster in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified Greenplum® cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified Greenplum® cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Start(self, request, context):
        """Starts the specified Greenplum® cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stop(self, request, context):
        """Stops the specified Greenplum® cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Retrieves the list of Operation resources for the specified cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMasterHosts(self, request, context):
        """Retrieves a list of master hosts for the specified cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSegmentHosts(self, request, context):
        """Retrieves a list of segment hosts for the specified cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListLogs(self, request, context):
        """Retrieves logs for the specified Greenplum® cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBackups(self, request, context):
        """Retrieves the list of available backups for the specified Greenplum cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Restore(self, request, context):
        """Creates a new Greenplum® cluster using the specified backup.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClusterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.GetClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__pb2.Cluster.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClustersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClustersResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.CreateClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.UpdateClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.DeleteClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Start': grpc.unary_unary_rpc_method_handler(
                    servicer.Start,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.StartClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Stop': grpc.unary_unary_rpc_method_handler(
                    servicer.Stop,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.StopClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterOperationsResponse.SerializeToString,
            ),
            'ListMasterHosts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListMasterHosts,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterHostsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterHostsResponse.SerializeToString,
            ),
            'ListSegmentHosts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSegmentHosts,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterHostsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterHostsResponse.SerializeToString,
            ),
            'ListLogs': grpc.unary_unary_rpc_method_handler(
                    servicer.ListLogs,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterLogsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterLogsResponse.SerializeToString,
            ),
            'ListBackups': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBackups,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterBackupsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterBackupsResponse.SerializeToString,
            ),
            'Restore': grpc.unary_unary_rpc_method_handler(
                    servicer.Restore,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.RestoreClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.mdb.greenplum.v1.ClusterService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClusterService(object):
    """A set of methods for managing Greenplum® clusters.
    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.greenplum.v1.ClusterService/Get',
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.GetClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__pb2.Cluster.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.greenplum.v1.ClusterService/List',
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClustersRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClustersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.greenplum.v1.ClusterService/Create',
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.CreateClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.greenplum.v1.ClusterService/Update',
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.UpdateClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.greenplum.v1.ClusterService/Delete',
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.DeleteClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Start(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.greenplum.v1.ClusterService/Start',
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.StartClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.greenplum.v1.ClusterService/Stop',
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.StopClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.greenplum.v1.ClusterService/ListOperations',
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterOperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListMasterHosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.greenplum.v1.ClusterService/ListMasterHosts',
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterHostsRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterHostsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSegmentHosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.greenplum.v1.ClusterService/ListSegmentHosts',
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterHostsRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterHostsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListLogs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.greenplum.v1.ClusterService/ListLogs',
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterLogsRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterLogsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListBackups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.greenplum.v1.ClusterService/ListBackups',
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterBackupsRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.ListClusterBackupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Restore(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.greenplum.v1.ClusterService/Restore',
            yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__service__pb2.RestoreClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
