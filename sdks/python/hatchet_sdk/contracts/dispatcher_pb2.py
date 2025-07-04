# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dispatcher.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x64ispatcher.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"V\n\x0cWorkerLabels\x12\x15\n\x08strValue\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08intValue\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\x0b\n\t_strValueB\x0b\n\t_intValue\"\xc8\x01\n\x0bRuntimeInfo\x12\x17\n\nsdkVersion\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1c\n\x08language\x18\x02 \x01(\x0e\x32\x05.SDKSH\x01\x88\x01\x01\x12\x1c\n\x0flanguageVersion\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x0f\n\x02os\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x05 \x01(\tH\x04\x88\x01\x01\x42\r\n\x0b_sdkVersionB\x0b\n\t_languageB\x12\n\x10_languageVersionB\x05\n\x03_osB\x08\n\x06_extra\"\xc0\x02\n\x15WorkerRegisterRequest\x12\x12\n\nworkerName\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x63tions\x18\x02 \x03(\t\x12\x10\n\x08services\x18\x03 \x03(\t\x12\x14\n\x07maxRuns\x18\x04 \x01(\x05H\x00\x88\x01\x01\x12\x32\n\x06labels\x18\x05 \x03(\x0b\x32\".WorkerRegisterRequest.LabelsEntry\x12\x16\n\twebhookId\x18\x06 \x01(\tH\x01\x88\x01\x01\x12&\n\x0bruntimeInfo\x18\x07 \x01(\x0b\x32\x0c.RuntimeInfoH\x02\x88\x01\x01\x1a<\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.WorkerLabels:\x02\x38\x01\x42\n\n\x08_maxRunsB\x0c\n\n_webhookIdB\x0e\n\x0c_runtimeInfo\"P\n\x16WorkerRegisterResponse\x12\x10\n\x08tenantId\x18\x01 \x01(\t\x12\x10\n\x08workerId\x18\x02 \x01(\t\x12\x12\n\nworkerName\x18\x03 \x01(\t\"\xa3\x01\n\x19UpsertWorkerLabelsRequest\x12\x10\n\x08workerId\x18\x01 \x01(\t\x12\x36\n\x06labels\x18\x02 \x03(\x0b\x32&.UpsertWorkerLabelsRequest.LabelsEntry\x1a<\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.WorkerLabels:\x02\x38\x01\"@\n\x1aUpsertWorkerLabelsResponse\x12\x10\n\x08tenantId\x18\x01 \x01(\t\x12\x10\n\x08workerId\x18\x02 \x01(\t\"\xf6\x04\n\x0e\x41ssignedAction\x12\x10\n\x08tenantId\x18\x01 \x01(\t\x12\x15\n\rworkflowRunId\x18\x02 \x01(\t\x12\x18\n\x10getGroupKeyRunId\x18\x03 \x01(\t\x12\r\n\x05jobId\x18\x04 \x01(\t\x12\x0f\n\x07jobName\x18\x05 \x01(\t\x12\x10\n\x08jobRunId\x18\x06 \x01(\t\x12\x0e\n\x06stepId\x18\x07 \x01(\t\x12\x11\n\tstepRunId\x18\x08 \x01(\t\x12\x10\n\x08\x61\x63tionId\x18\t \x01(\t\x12\x1f\n\nactionType\x18\n \x01(\x0e\x32\x0b.ActionType\x12\x15\n\ractionPayload\x18\x0b \x01(\t\x12\x10\n\x08stepName\x18\x0c \x01(\t\x12\x12\n\nretryCount\x18\r \x01(\x05\x12 \n\x13\x61\x64\x64itional_metadata\x18\x0e \x01(\tH\x00\x88\x01\x01\x12!\n\x14\x63hild_workflow_index\x18\x0f \x01(\x05H\x01\x88\x01\x01\x12\x1f\n\x12\x63hild_workflow_key\x18\x10 \x01(\tH\x02\x88\x01\x01\x12#\n\x16parent_workflow_run_id\x18\x11 \x01(\tH\x03\x88\x01\x01\x12\x10\n\x08priority\x18\x12 \x01(\x05\x12\x17\n\nworkflowId\x18\x13 \x01(\tH\x04\x88\x01\x01\x12\x1e\n\x11workflowVersionId\x18\x14 \x01(\tH\x05\x88\x01\x01\x42\x16\n\x14_additional_metadataB\x17\n\x15_child_workflow_indexB\x15\n\x13_child_workflow_keyB\x19\n\x17_parent_workflow_run_idB\r\n\x0b_workflowIdB\x14\n\x12_workflowVersionId\"\'\n\x13WorkerListenRequest\x12\x10\n\x08workerId\x18\x01 \x01(\t\",\n\x18WorkerUnsubscribeRequest\x12\x10\n\x08workerId\x18\x01 \x01(\t\"?\n\x19WorkerUnsubscribeResponse\x12\x10\n\x08tenantId\x18\x01 \x01(\t\x12\x10\n\x08workerId\x18\x02 \x01(\t\"\xe1\x01\n\x13GroupKeyActionEvent\x12\x10\n\x08workerId\x18\x01 \x01(\t\x12\x15\n\rworkflowRunId\x18\x02 \x01(\t\x12\x18\n\x10getGroupKeyRunId\x18\x03 \x01(\t\x12\x10\n\x08\x61\x63tionId\x18\x04 \x01(\t\x12\x32\n\x0e\x65ventTimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\teventType\x18\x06 \x01(\x0e\x32\x18.GroupKeyActionEventType\x12\x14\n\x0c\x65ventPayload\x18\x07 \x01(\t\"\xc4\x02\n\x0fStepActionEvent\x12\x10\n\x08workerId\x18\x01 \x01(\t\x12\r\n\x05jobId\x18\x02 \x01(\t\x12\x10\n\x08jobRunId\x18\x03 \x01(\t\x12\x0e\n\x06stepId\x18\x04 \x01(\t\x12\x11\n\tstepRunId\x18\x05 \x01(\t\x12\x10\n\x08\x61\x63tionId\x18\x06 \x01(\t\x12\x32\n\x0e\x65ventTimestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\teventType\x18\x08 \x01(\x0e\x32\x14.StepActionEventType\x12\x14\n\x0c\x65ventPayload\x18\t \x01(\t\x12\x17\n\nretryCount\x18\n \x01(\x05H\x00\x88\x01\x01\x12\x1b\n\x0eshouldNotRetry\x18\x0b \x01(\x08H\x01\x88\x01\x01\x42\r\n\x0b_retryCountB\x11\n\x0f_shouldNotRetry\"9\n\x13\x41\x63tionEventResponse\x12\x10\n\x08tenantId\x18\x01 \x01(\t\x12\x10\n\x08workerId\x18\x02 \x01(\t\"\xc0\x01\n SubscribeToWorkflowEventsRequest\x12\x1a\n\rworkflowRunId\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1e\n\x11\x61\x64\x64itionalMetaKey\x18\x02 \x01(\tH\x01\x88\x01\x01\x12 \n\x13\x61\x64\x64itionalMetaValue\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x10\n\x0e_workflowRunIdB\x14\n\x12_additionalMetaKeyB\x16\n\x14_additionalMetaValue\"7\n\x1eSubscribeToWorkflowRunsRequest\x12\x15\n\rworkflowRunId\x18\x01 \x01(\t\"\xda\x02\n\rWorkflowEvent\x12\x15\n\rworkflowRunId\x18\x01 \x01(\t\x12#\n\x0cresourceType\x18\x02 \x01(\x0e\x32\r.ResourceType\x12%\n\teventType\x18\x03 \x01(\x0e\x32\x12.ResourceEventType\x12\x12\n\nresourceId\x18\x04 \x01(\t\x12\x32\n\x0e\x65ventTimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0c\x65ventPayload\x18\x06 \x01(\t\x12\x0e\n\x06hangup\x18\x07 \x01(\x08\x12\x18\n\x0bstepRetries\x18\x08 \x01(\x05H\x00\x88\x01\x01\x12\x17\n\nretryCount\x18\t \x01(\x05H\x01\x88\x01\x01\x12\x17\n\neventIndex\x18\n \x01(\x03H\x02\x88\x01\x01\x42\x0e\n\x0c_stepRetriesB\r\n\x0b_retryCountB\r\n\x0b_eventIndex\"\xa8\x01\n\x10WorkflowRunEvent\x12\x15\n\rworkflowRunId\x18\x01 \x01(\t\x12(\n\teventType\x18\x02 \x01(\x0e\x32\x15.WorkflowRunEventType\x12\x32\n\x0e\x65ventTimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1f\n\x07results\x18\x04 \x03(\x0b\x32\x0e.StepRunResult\"\x8a\x01\n\rStepRunResult\x12\x11\n\tstepRunId\x18\x01 \x01(\t\x12\x16\n\x0estepReadableId\x18\x02 \x01(\t\x12\x10\n\x08jobRunId\x18\x03 \x01(\t\x12\x12\n\x05\x65rror\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06output\x18\x05 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_errorB\t\n\x07_output\"W\n\rOverridesData\x12\x11\n\tstepRunId\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x16\n\x0e\x63\x61llerFilename\x18\x04 \x01(\t\"\x17\n\x15OverridesDataResponse\"U\n\x10HeartbeatRequest\x12\x10\n\x08workerId\x18\x01 \x01(\t\x12/\n\x0bheartbeatAt\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x13\n\x11HeartbeatResponse\"F\n\x15RefreshTimeoutRequest\x12\x11\n\tstepRunId\x18\x01 \x01(\t\x12\x1a\n\x12incrementTimeoutBy\x18\x02 \x01(\t\"G\n\x16RefreshTimeoutResponse\x12-\n\ttimeoutAt\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\'\n\x12ReleaseSlotRequest\x12\x11\n\tstepRunId\x18\x01 \x01(\t\"\x15\n\x13ReleaseSlotResponse*7\n\x04SDKS\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02GO\x10\x01\x12\n\n\x06PYTHON\x10\x02\x12\x0e\n\nTYPESCRIPT\x10\x03*N\n\nActionType\x12\x12\n\x0eSTART_STEP_RUN\x10\x00\x12\x13\n\x0f\x43\x41NCEL_STEP_RUN\x10\x01\x12\x17\n\x13START_GET_GROUP_KEY\x10\x02*\xa2\x01\n\x17GroupKeyActionEventType\x12 \n\x1cGROUP_KEY_EVENT_TYPE_UNKNOWN\x10\x00\x12 \n\x1cGROUP_KEY_EVENT_TYPE_STARTED\x10\x01\x12\"\n\x1eGROUP_KEY_EVENT_TYPE_COMPLETED\x10\x02\x12\x1f\n\x1bGROUP_KEY_EVENT_TYPE_FAILED\x10\x03*\xac\x01\n\x13StepActionEventType\x12\x1b\n\x17STEP_EVENT_TYPE_UNKNOWN\x10\x00\x12\x1b\n\x17STEP_EVENT_TYPE_STARTED\x10\x01\x12\x1d\n\x19STEP_EVENT_TYPE_COMPLETED\x10\x02\x12\x1a\n\x16STEP_EVENT_TYPE_FAILED\x10\x03\x12 \n\x1cSTEP_EVENT_TYPE_ACKNOWLEDGED\x10\x04*e\n\x0cResourceType\x12\x19\n\x15RESOURCE_TYPE_UNKNOWN\x10\x00\x12\x1a\n\x16RESOURCE_TYPE_STEP_RUN\x10\x01\x12\x1e\n\x1aRESOURCE_TYPE_WORKFLOW_RUN\x10\x02*\xfe\x01\n\x11ResourceEventType\x12\x1f\n\x1bRESOURCE_EVENT_TYPE_UNKNOWN\x10\x00\x12\x1f\n\x1bRESOURCE_EVENT_TYPE_STARTED\x10\x01\x12!\n\x1dRESOURCE_EVENT_TYPE_COMPLETED\x10\x02\x12\x1e\n\x1aRESOURCE_EVENT_TYPE_FAILED\x10\x03\x12!\n\x1dRESOURCE_EVENT_TYPE_CANCELLED\x10\x04\x12!\n\x1dRESOURCE_EVENT_TYPE_TIMED_OUT\x10\x05\x12\x1e\n\x1aRESOURCE_EVENT_TYPE_STREAM\x10\x06*<\n\x14WorkflowRunEventType\x12$\n WORKFLOW_RUN_EVENT_TYPE_FINISHED\x10\x00\x32\xf8\x06\n\nDispatcher\x12=\n\x08Register\x12\x16.WorkerRegisterRequest\x1a\x17.WorkerRegisterResponse\"\x00\x12\x33\n\x06Listen\x12\x14.WorkerListenRequest\x1a\x0f.AssignedAction\"\x00\x30\x01\x12\x35\n\x08ListenV2\x12\x14.WorkerListenRequest\x1a\x0f.AssignedAction\"\x00\x30\x01\x12\x34\n\tHeartbeat\x12\x11.HeartbeatRequest\x1a\x12.HeartbeatResponse\"\x00\x12R\n\x19SubscribeToWorkflowEvents\x12!.SubscribeToWorkflowEventsRequest\x1a\x0e.WorkflowEvent\"\x00\x30\x01\x12S\n\x17SubscribeToWorkflowRuns\x12\x1f.SubscribeToWorkflowRunsRequest\x1a\x11.WorkflowRunEvent\"\x00(\x01\x30\x01\x12?\n\x13SendStepActionEvent\x12\x10.StepActionEvent\x1a\x14.ActionEventResponse\"\x00\x12G\n\x17SendGroupKeyActionEvent\x12\x14.GroupKeyActionEvent\x1a\x14.ActionEventResponse\"\x00\x12<\n\x10PutOverridesData\x12\x0e.OverridesData\x1a\x16.OverridesDataResponse\"\x00\x12\x46\n\x0bUnsubscribe\x12\x19.WorkerUnsubscribeRequest\x1a\x1a.WorkerUnsubscribeResponse\"\x00\x12\x43\n\x0eRefreshTimeout\x12\x16.RefreshTimeoutRequest\x1a\x17.RefreshTimeoutResponse\"\x00\x12:\n\x0bReleaseSlot\x12\x13.ReleaseSlotRequest\x1a\x14.ReleaseSlotResponse\"\x00\x12O\n\x12UpsertWorkerLabels\x12\x1a.UpsertWorkerLabelsRequest\x1a\x1b.UpsertWorkerLabelsResponse\"\x00\x42GZEgithub.com/hatchet-dev/hatchet/internal/services/dispatcher/contractsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dispatcher_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZEgithub.com/hatchet-dev/hatchet/internal/services/dispatcher/contracts'
  _globals['_WORKERREGISTERREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_WORKERREGISTERREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPSERTWORKERLABELSREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPSERTWORKERLABELSREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_SDKS']._serialized_start=3724
  _globals['_SDKS']._serialized_end=3779
  _globals['_ACTIONTYPE']._serialized_start=3781
  _globals['_ACTIONTYPE']._serialized_end=3859
  _globals['_GROUPKEYACTIONEVENTTYPE']._serialized_start=3862
  _globals['_GROUPKEYACTIONEVENTTYPE']._serialized_end=4024
  _globals['_STEPACTIONEVENTTYPE']._serialized_start=4027
  _globals['_STEPACTIONEVENTTYPE']._serialized_end=4199
  _globals['_RESOURCETYPE']._serialized_start=4201
  _globals['_RESOURCETYPE']._serialized_end=4302
  _globals['_RESOURCEEVENTTYPE']._serialized_start=4305
  _globals['_RESOURCEEVENTTYPE']._serialized_end=4559
  _globals['_WORKFLOWRUNEVENTTYPE']._serialized_start=4561
  _globals['_WORKFLOWRUNEVENTTYPE']._serialized_end=4621
  _globals['_WORKERLABELS']._serialized_start=53
  _globals['_WORKERLABELS']._serialized_end=139
  _globals['_RUNTIMEINFO']._serialized_start=142
  _globals['_RUNTIMEINFO']._serialized_end=342
  _globals['_WORKERREGISTERREQUEST']._serialized_start=345
  _globals['_WORKERREGISTERREQUEST']._serialized_end=665
  _globals['_WORKERREGISTERREQUEST_LABELSENTRY']._serialized_start=563
  _globals['_WORKERREGISTERREQUEST_LABELSENTRY']._serialized_end=623
  _globals['_WORKERREGISTERRESPONSE']._serialized_start=667
  _globals['_WORKERREGISTERRESPONSE']._serialized_end=747
  _globals['_UPSERTWORKERLABELSREQUEST']._serialized_start=750
  _globals['_UPSERTWORKERLABELSREQUEST']._serialized_end=913
  _globals['_UPSERTWORKERLABELSREQUEST_LABELSENTRY']._serialized_start=563
  _globals['_UPSERTWORKERLABELSREQUEST_LABELSENTRY']._serialized_end=623
  _globals['_UPSERTWORKERLABELSRESPONSE']._serialized_start=915
  _globals['_UPSERTWORKERLABELSRESPONSE']._serialized_end=979
  _globals['_ASSIGNEDACTION']._serialized_start=982
  _globals['_ASSIGNEDACTION']._serialized_end=1612
  _globals['_WORKERLISTENREQUEST']._serialized_start=1614
  _globals['_WORKERLISTENREQUEST']._serialized_end=1653
  _globals['_WORKERUNSUBSCRIBEREQUEST']._serialized_start=1655
  _globals['_WORKERUNSUBSCRIBEREQUEST']._serialized_end=1699
  _globals['_WORKERUNSUBSCRIBERESPONSE']._serialized_start=1701
  _globals['_WORKERUNSUBSCRIBERESPONSE']._serialized_end=1764
  _globals['_GROUPKEYACTIONEVENT']._serialized_start=1767
  _globals['_GROUPKEYACTIONEVENT']._serialized_end=1992
  _globals['_STEPACTIONEVENT']._serialized_start=1995
  _globals['_STEPACTIONEVENT']._serialized_end=2319
  _globals['_ACTIONEVENTRESPONSE']._serialized_start=2321
  _globals['_ACTIONEVENTRESPONSE']._serialized_end=2378
  _globals['_SUBSCRIBETOWORKFLOWEVENTSREQUEST']._serialized_start=2381
  _globals['_SUBSCRIBETOWORKFLOWEVENTSREQUEST']._serialized_end=2573
  _globals['_SUBSCRIBETOWORKFLOWRUNSREQUEST']._serialized_start=2575
  _globals['_SUBSCRIBETOWORKFLOWRUNSREQUEST']._serialized_end=2630
  _globals['_WORKFLOWEVENT']._serialized_start=2633
  _globals['_WORKFLOWEVENT']._serialized_end=2979
  _globals['_WORKFLOWRUNEVENT']._serialized_start=2982
  _globals['_WORKFLOWRUNEVENT']._serialized_end=3150
  _globals['_STEPRUNRESULT']._serialized_start=3153
  _globals['_STEPRUNRESULT']._serialized_end=3291
  _globals['_OVERRIDESDATA']._serialized_start=3293
  _globals['_OVERRIDESDATA']._serialized_end=3380
  _globals['_OVERRIDESDATARESPONSE']._serialized_start=3382
  _globals['_OVERRIDESDATARESPONSE']._serialized_end=3405
  _globals['_HEARTBEATREQUEST']._serialized_start=3407
  _globals['_HEARTBEATREQUEST']._serialized_end=3492
  _globals['_HEARTBEATRESPONSE']._serialized_start=3494
  _globals['_HEARTBEATRESPONSE']._serialized_end=3513
  _globals['_REFRESHTIMEOUTREQUEST']._serialized_start=3515
  _globals['_REFRESHTIMEOUTREQUEST']._serialized_end=3585
  _globals['_REFRESHTIMEOUTRESPONSE']._serialized_start=3587
  _globals['_REFRESHTIMEOUTRESPONSE']._serialized_end=3658
  _globals['_RELEASESLOTREQUEST']._serialized_start=3660
  _globals['_RELEASESLOTREQUEST']._serialized_end=3699
  _globals['_RELEASESLOTRESPONSE']._serialized_start=3701
  _globals['_RELEASESLOTRESPONSE']._serialized_end=3722
  _globals['_DISPATCHER']._serialized_start=4624
  _globals['_DISPATCHER']._serialized_end=5512
# @@protoc_insertion_point(module_scope)
