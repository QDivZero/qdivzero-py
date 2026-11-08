"""Contains all the data models used in inputs/outputs"""

from .accept_invitation_request import AcceptInvitationRequest
from .account_balance_response import AccountBalanceResponse
from .account_list_response import AccountListResponse
from .account_member_list_response import AccountMemberListResponse
from .account_member_response import AccountMemberResponse
from .account_membership_response import AccountMembershipResponse
from .account_response import AccountResponse
from .add_account_member_request import AddAccountMemberRequest
from .api_key_list_response import ApiKeyListResponse
from .api_key_response import ApiKeyResponse
from .audio_speech_request import AudioSpeechRequest
from .begin_passkey_registration_response import BeginPasskeyRegistrationResponse
from .begin_passkeylogin_request import BeginPasskeyloginRequest
from .begin_passkeylogin_response import BeginPasskeyloginResponse
from .begin_totp_enrollment_response import BeginTotpEnrollmentResponse
from .biomolecular_capabilities import BiomolecularCapabilities
from .catalog_gpu_response import CatalogGPUResponse
from .change_password_request import ChangePasswordRequest
from .chat_message_envelope import ChatMessageEnvelope
from .chat_request_envelope import ChatRequestEnvelope
from .chat_tool_call_envelope import ChatToolCallEnvelope
from .chat_tool_call_function_envelope import ChatToolCallFunctionEnvelope
from .checkout_session_response import CheckoutSessionResponse
from .confirm_totp_enrollment_request import ConfirmTotpEnrollmentRequest
from .create_account_request import CreateAccountRequest
from .create_checkout_session_request import CreateCheckoutSessionRequest
from .create_firewall_request import CreateFirewallRequest
from .create_firewall_rule_request import CreateFirewallRuleRequest
from .create_instance_request import CreateInstanceRequest
from .create_instance_request_workload_kind import CreateInstanceRequestWorkloadKind
from .create_invitation_request import CreateInvitationRequest
from .create_serving_endpoint_request import CreateServingEndpointRequest
from .create_smart_balancer_request import CreateSmartBalancerRequest
from .create_target_group_request import CreateTargetGroupRequest
from .create_vector_database_request import CreateVectorDatabaseRequest
from .debit_balance_request import DebitBalanceRequest
from .debit_balance_response import DebitBalanceResponse
from .debit_operation_response import DebitOperationResponse
from .delete_firewall_response_200 import DeleteFirewallResponse200
from .delete_firewall_rule_response_200 import DeleteFirewallRuleResponse200
from .delete_v1_responses_session_response_200 import DeleteV1ResponsesSessionResponse200
from .delete_v1_responses_sessions_response_200 import DeleteV1ResponsesSessionsResponse200
from .delete_vector_database_response_200 import DeleteVectorDatabaseResponse200
from .detection_stream_error import DetectionStreamError
from .detection_stream_event import DetectionStreamEvent
from .detection_stream_options import DetectionStreamOptions
from .dismiss_request import DismissRequest
from .dismiss_response import DismissResponse
from .embeddings_request_envelope import EmbeddingsRequestEnvelope
from .enable_shared_capacity_request import EnableSharedCapacityRequest
from .error_response import ErrorResponse
from .execution_decision_choice_answer import ExecutionDecisionChoiceAnswer
from .execution_decision_choice_answer_probabilities import ExecutionDecisionChoiceAnswerProbabilities
from .execution_decision_choice_answer_type import ExecutionDecisionChoiceAnswerType
from .execution_decision_choice_question import ExecutionDecisionChoiceQuestion
from .execution_decision_choice_question_criteria import ExecutionDecisionChoiceQuestionCriteria
from .execution_decision_choice_question_type import ExecutionDecisionChoiceQuestionType
from .execution_decision_diagnostics import ExecutionDecisionDiagnostics
from .execution_decision_noul_answer import ExecutionDecisionNoulAnswer
from .execution_decision_noul_answer_probabilities_type_0 import ExecutionDecisionNoulAnswerProbabilitiesType0
from .execution_decision_noul_answer_probabilities_type_1 import ExecutionDecisionNoulAnswerProbabilitiesType1
from .execution_decision_noul_answer_type import ExecutionDecisionNoulAnswerType
from .execution_decision_noul_question import ExecutionDecisionNoulQuestion
from .execution_decision_noul_question_criteria_type_0 import ExecutionDecisionNoulQuestionCriteriaType0
from .execution_decision_noul_question_type import ExecutionDecisionNoulQuestionType
from .execution_decision_score_answer import ExecutionDecisionScoreAnswer
from .execution_decision_score_answer_legend import ExecutionDecisionScoreAnswerLegend
from .execution_decision_score_answer_probabilities import ExecutionDecisionScoreAnswerProbabilities
from .execution_decision_score_answer_type import ExecutionDecisionScoreAnswerType
from .execution_decision_score_question import ExecutionDecisionScoreQuestion
from .execution_decision_score_question_type import ExecutionDecisionScoreQuestionType
from .execution_decision_usage import ExecutionDecisionUsage
from .execution_forecast_input import ExecutionForecastInput
from .execution_forecast_prediction import ExecutionForecastPrediction
from .execution_forecast_request import ExecutionForecastRequest
from .execution_forecast_response import ExecutionForecastResponse
from .execution_system_one_request import ExecutionSystemOneRequest
from .execution_system_one_request_questions import ExecutionSystemOneRequestQuestions
from .execution_system_one_request_state_type_1 import ExecutionSystemOneRequestStateType1
from .execution_system_one_response import ExecutionSystemOneResponse
from .execution_system_one_response_answers import ExecutionSystemOneResponseAnswers
from .execution_system_one_response_diagnostics import ExecutionSystemOneResponseDiagnostics
from .finish_passkey_registration_request import FinishPasskeyRegistrationRequest
from .finish_passkeylogin_request import FinishPasskeyloginRequest
from .finish_passkeylogin_response import FinishPasskeyloginResponse
from .firewall_evaluation_request import FirewallEvaluationRequest
from .firewall_evaluation_response import FirewallEvaluationResponse
from .firewall_response import FirewallResponse
from .firewall_rule_evaluation_request import FirewallRuleEvaluationRequest
from .firewall_rule_response import FirewallRuleResponse
from .forgot_password_request import ForgotPasswordRequest
from .forgot_password_response import ForgotPasswordResponse
from .get_auth_oauth_identities_response_200 import GetAuthOauthIdentitiesResponse200
from .get_instance_usage_range import GetInstanceUsageRange
from .get_serving_endpoints_response_200 import GetServingEndpointsResponse200
from .get_smart_balancers_response_200 import GetSmartBalancersResponse200
from .get_target_groups_response_200 import GetTargetGroupsResponse200
from .get_template_by_slug_response import GetTemplateBySlugResponse
from .get_tools_response_200 import GetToolsResponse200
from .get_user_variant_response import GetUserVariantResponse
from .get_v1_audio_voices_response_200 import GetV1AudioVoicesResponse200
from .get_v1_models_response_200 import GetV1ModelsResponse200
from .get_v1_public_token_usage_response_200 import GetV1PublicTokenUsageResponse200
from .get_v1_public_token_usage_response_200_days_item import GetV1PublicTokenUsageResponse200DaysItem
from .get_v1_public_token_usage_response_200_period_totals import GetV1PublicTokenUsageResponse200PeriodTotals
from .get_v1_public_token_usage_response_200_totals import GetV1PublicTokenUsageResponse200Totals
from .get_v1_responses_session_detail_response_200 import GetV1ResponsesSessionDetailResponse200
from .get_v1_responses_sessions_list_response_200 import GetV1ResponsesSessionsListResponse200
from .get_v1_responses_sessions_status_response_200 import GetV1ResponsesSessionsStatusResponse200
from .gpu_list_response import GpuListResponse
from .gpu_preference_response import GpuPreferenceResponse
from .http_target import HttpTarget
from .http_target_labels import HttpTargetLabels
from .hugging_face_file_response import HuggingFaceFileResponse
from .hugging_face_files_response import HuggingFaceFilesResponse
from .hugging_face_gguf_file_response import HuggingFaceGGUFFileResponse
from .hugging_face_model_response import HuggingFaceModelResponse
from .hugging_face_models_response import HuggingFaceModelsResponse
from .hugging_face_org_info_response import HuggingFaceOrgInfoResponse
from .hugging_face_yolo_file_response import HuggingFaceYOLOFileResponse
from .image_detection_box_output import ImageDetectionBoxOutput
from .image_detection_keypoint_output import ImageDetectionKeypointOutput
from .image_detection_output import ImageDetectionOutput
from .image_detection_result_output import ImageDetectionResultOutput
from .image_generation_request import ImageGenerationRequest
from .impersonation_info import ImpersonationInfo
from .index_document_request import IndexDocumentRequest
from .index_document_request_metadata import IndexDocumentRequestMetadata
from .index_document_source_request import IndexDocumentSourceRequest
from .index_documents_request import IndexDocumentsRequest
from .index_job_response import IndexJobResponse
from .instance_list_response import InstanceListResponse
from .instance_response import InstanceResponse
from .instance_usage_bucket_response import InstanceUsageBucketResponse
from .instance_usage_response import InstanceUsageResponse
from .instance_usage_summary_response import InstanceUsageSummaryResponse
from .invitation_list_response import InvitationListResponse
from .invitation_response import InvitationResponse
from .join_shared_capacity_request import JoinSharedCapacityRequest
from .ledger_entry_response import LedgerEntryResponse
from .ledger_history_response import LedgerHistoryResponse
from .legal_acceptance_item import LegalAcceptanceItem
from .legal_acceptance_request import LegalAcceptanceRequest
from .list_documents_response import ListDocumentsResponse
from .list_notifications_response import ListNotificationsResponse
from .list_user_variants_response import ListUserVariantsResponse
from .listed_document_response import ListedDocumentResponse
from .listed_document_response_metadata import ListedDocumentResponseMetadata
from .login_request import LoginRequest
from .login_response import LoginResponse
from .mark_all_read_request import MarkAllReadRequest
from .mark_all_read_response import MarkAllReadResponse
from .model import Model
from .model_prices_response import ModelPricesResponse
from .notification_link_response import NotificationLinkResponse
from .notification_link_response_route_args import NotificationLinkResponseRouteArgs
from .notification_response import NotificationResponse
from .notification_response_body_args import NotificationResponseBodyArgs
from .notification_response_metadata import NotificationResponseMetadata
from .notification_response_title_args import NotificationResponseTitleArgs
from .oauth_signup_request import OauthSignupRequest
from .oauth_totp_request import OauthTOTPRequest
from .passkey_list_response import PasskeyListResponse
from .passkey_response import PasskeyResponse
from .payment_response import PaymentResponse
from .payments_response import PaymentsResponse
from .post_auth_oauth_signup_response_200 import PostAuthOauthSignupResponse200
from .post_auth_oauth_totp_response_200 import PostAuthOauthTotpResponse200
from .post_ollama_show_body import PostOllamaShowBody
from .post_ollama_show_response_200 import PostOllamaShowResponse200
from .post_runtime_notify_crash_body import PostRuntimeNotifyCrashBody
from .post_runtime_notify_progress_response_200 import PostRuntimeNotifyProgressResponse200
from .post_serving_endpoint_response_409 import PostServingEndpointResponse409
from .post_v1_audio_transcriptions_body import PostV1AudioTranscriptionsBody
from .post_v1_audio_transcriptions_response_200 import PostV1AudioTranscriptionsResponse200
from .post_v1_chat_completions_response_200 import PostV1ChatCompletionsResponse200
from .post_v1_chat_completions_response_403 import PostV1ChatCompletionsResponse403
from .post_v1_embeddings_response_200 import PostV1EmbeddingsResponse200
from .post_v1_image_detections_body import PostV1ImageDetectionsBody
from .post_v1_image_edits_body import PostV1ImageEditsBody
from .post_v1_image_edits_response_200 import PostV1ImageEditsResponse200
from .post_v1_image_generations_response_200 import PostV1ImageGenerationsResponse200
from .post_v1_responses_compact_response_200 import PostV1ResponsesCompactResponse200
from .post_v1_responses_response_200 import PostV1ResponsesResponse200
from .post_v1_video_generations_files_body import PostV1VideoGenerationsFilesBody
from .post_v1_video_generations_files_body_aspect_ratio import PostV1VideoGenerationsFilesBodyAspectRatio
from .post_v1_video_generations_files_body_fps import PostV1VideoGenerationsFilesBodyFps
from .post_v1_video_generations_files_body_task import PostV1VideoGenerationsFilesBodyTask
from .post_v1_video_generations_json_body import PostV1VideoGenerationsJsonBody
from .post_v1_video_generations_json_body_aspect_ratio import PostV1VideoGenerationsJsonBodyAspectRatio
from .post_v1_video_generations_json_body_fps import PostV1VideoGenerationsJsonBodyFps
from .post_v1_video_generations_json_body_task import PostV1VideoGenerationsJsonBodyTask
from .post_v1_video_job_files_body import PostV1VideoJobFilesBody
from .post_v1_video_job_files_body_aspect_ratio import PostV1VideoJobFilesBodyAspectRatio
from .post_v1_video_job_files_body_fps import PostV1VideoJobFilesBodyFps
from .post_v1_video_job_files_body_task import PostV1VideoJobFilesBodyTask
from .post_v1_video_job_json_body import PostV1VideoJobJsonBody
from .post_v1_video_job_json_body_aspect_ratio import PostV1VideoJobJsonBodyAspectRatio
from .post_v1_video_job_json_body_fps import PostV1VideoJobJsonBodyFps
from .post_v1_video_job_json_body_task import PostV1VideoJobJsonBodyTask
from .post_vector_database_index_direct_response_200 import PostVectorDatabaseIndexDirectResponse200
from .post_vector_database_index_jobs_response_202 import PostVectorDatabaseIndexJobsResponse202
from .post_vector_database_view_element_response_200 import PostVectorDatabaseViewElementResponse200
from .preview_instance_request import PreviewInstanceRequest
from .preview_instance_request_workload_kind import PreviewInstanceRequestWorkloadKind
from .preview_instance_response import PreviewInstanceResponse
from .preview_instance_update_request import PreviewInstanceUpdateRequest
from .pricing_service import PricingService
from .pricing_status import PricingStatus
from .protocol_context_management import ProtocolContextManagement
from .public_endpoint_price_response import PublicEndpointPriceResponse
from .public_endpoint_response import PublicEndpointResponse
from .public_endpoints_response import PublicEndpointsResponse
from .public_gpu_preference_json import PublicGPUPreferenceJSON
from .public_pricing_availability import PublicPricingAvailability
from .public_pricing_gpu import PublicPricingGPU
from .public_pricing_response import PublicPricingResponse
from .public_pricing_service import PublicPricingService
from .public_token_usage_day import PublicTokenUsageDay
from .public_token_usage_response import PublicTokenUsageResponse
from .public_token_usage_total import PublicTokenUsageTotal
from .put_v1_responses_sessions_status_body import PutV1ResponsesSessionsStatusBody
from .put_v1_responses_sessions_status_response_200 import PutV1ResponsesSessionsStatusResponse200
from .queued_debit_response import QueuedDebitResponse
from .recommend_request import RecommendRequest
from .recommended_gpu import RecommendedGPU
from .refresh_response import RefreshResponse
from .register_passkey_request import RegisterPasskeyRequest
from .register_request import RegisterRequest
from .register_response import RegisterResponse
from .replica_set_list_response import ReplicaSetListResponse
from .replica_set_response import ReplicaSetResponse
from .resend_activation_email_request import ResendActivationEmailRequest
from .resend_email_response import ResendEmailResponse
from .resend_login_email_request import ResendLoginEmailRequest
from .reset_password_request import ResetPasswordRequest
from .reset_password_response import ResetPasswordResponse
from .resource_metric_snapshot import ResourceMetricSnapshot
from .resource_metrics_response import ResourceMetricsResponse
from .responses_request_envelope import ResponsesRequestEnvelope
from .responses_request_envelope_metadata import ResponsesRequestEnvelopeMetadata
from .responses_request_envelope_reasoning import ResponsesRequestEnvelopeReasoning
from .runtime_config_request import RuntimeConfigRequest
from .runtime_config_request_storage_mounts_item import RuntimeConfigRequestStorageMountsItem
from .runtime_config_response import RuntimeConfigResponse
from .runtime_config_response_storage_mounts_item import RuntimeConfigResponseStorageMountsItem
from .runtime_memory_estimate_response import RuntimeMemoryEstimateResponse
from .runtime_progress_request import RuntimeProgressRequest
from .scale_replica_set_request import ScaleReplicaSetRequest
from .schedule_rule_list_response import ScheduleRuleListResponse
from .schedule_rule_request import ScheduleRuleRequest
from .schedule_rule_response import ScheduleRuleResponse
from .search_hit_response import SearchHitResponse
from .search_hit_response_metadata import SearchHitResponseMetadata
from .search_hit_source_response import SearchHitSourceResponse
from .search_recommend_request import SearchRecommendRequest
from .search_request import SearchRequest
from .service_biomolecular_artifact import ServiceBiomolecularArtifact
from .service_biomolecular_attachment import ServiceBiomolecularAttachment
from .service_biomolecular_job_result import ServiceBiomolecularJobResult
from .service_biomolecular_job_result_affinity import ServiceBiomolecularJobResultAffinity
from .service_biomolecular_job_result_confidence_item import ServiceBiomolecularJobResultConfidenceItem
from .service_biomolecular_job_result_metadata import ServiceBiomolecularJobResultMetadata
from .service_biomolecular_options import ServiceBiomolecularOptions
from .service_biomolecular_submit_request import ServiceBiomolecularSubmitRequest
from .service_biomolecular_submit_request_input import ServiceBiomolecularSubmitRequestInput
from .service_video_job_content_url import ServiceVideoJobContentURL
from .service_video_job_result import ServiceVideoJobResult
from .service_video_job_result_status import ServiceVideoJobResultStatus
from .serving_endpoint_response import ServingEndpointResponse
from .serving_provider_response import ServingProviderResponse
from .serving_target_request import ServingTargetRequest
from .serving_target_response import ServingTargetResponse
from .shared_capacity_instance_response import SharedCapacityInstanceResponse
from .shared_capacity_link_response import SharedCapacityLinkResponse
from .shared_capacity_list_response import SharedCapacityListResponse
from .shared_capacity_membership_response import SharedCapacityMembershipResponse
from .shared_capacity_public_list_response import SharedCapacityPublicListResponse
from .shared_capacity_public_response import SharedCapacityPublicResponse
from .shared_capacity_response import SharedCapacityResponse
from .smart_balancer_route_destination_request import SmartBalancerRouteDestinationRequest
from .smart_balancer_route_destination_response import SmartBalancerRouteDestinationResponse
from .smart_balancer_route_request import SmartBalancerRouteRequest
from .smart_balancer_route_response import SmartBalancerRouteResponse
from .smart_balancer_router_model_request import SmartBalancerRouterModelRequest
from .smart_balancer_router_model_response import SmartBalancerRouterModelResponse
from .smart_balancer_view_response import SmartBalancerViewResponse
from .startup_progress import StartupProgress
from .target_group_member_request import TargetGroupMemberRequest
from .target_group_member_response import TargetGroupMemberResponse
from .target_group_response import TargetGroupResponse
from .template import Template
from .template_with_variants import TemplateWithVariants
from .timestamp import Timestamp
from .translation import Translation
from .try_tool_body import TryToolBody
from .try_tool_response_200 import TryToolResponse200
from .tutorial_progress_response import TutorialProgressResponse
from .unread_count_response import UnreadCountResponse
from .unread_count_response_by_severity import UnreadCountResponseBySeverity
from .update_account_member_request import UpdateAccountMemberRequest
from .update_account_request import UpdateAccountRequest
from .update_firewall_request import UpdateFirewallRequest
from .update_firewall_rule_request import UpdateFirewallRuleRequest
from .update_instance_request import UpdateInstanceRequest
from .update_preferences_request import UpdatePreferencesRequest
from .update_replica_set_request import UpdateReplicaSetRequest
from .update_smart_balancer_request import UpdateSmartBalancerRequest
from .update_target_group_request import UpdateTargetGroupRequest
from .update_tutorial_progress_request import UpdateTutorialProgressRequest
from .update_vector_database_request import UpdateVectorDatabaseRequest
from .user_info_response import UserInfoResponse
from .user_preferences_response import UserPreferencesResponse
from .variant import Variant
from .variant_translation import VariantTranslation
from .variant_with_relations import VariantWithRelations
from .vector_database_response import VectorDatabaseResponse
from .verify_email_response import VerifyEmailResponse
from .video_jobs_list_response import VideoJobsListResponse
from .view_element_request import ViewElementRequest

__all__ = (
    "AcceptInvitationRequest",
    "AccountBalanceResponse",
    "AccountListResponse",
    "AccountMemberListResponse",
    "AccountMemberResponse",
    "AccountMembershipResponse",
    "AccountResponse",
    "AddAccountMemberRequest",
    "ApiKeyListResponse",
    "ApiKeyResponse",
    "AudioSpeechRequest",
    "BeginPasskeyloginRequest",
    "BeginPasskeyloginResponse",
    "BeginPasskeyRegistrationResponse",
    "BeginTotpEnrollmentResponse",
    "BiomolecularCapabilities",
    "CatalogGPUResponse",
    "ChangePasswordRequest",
    "ChatMessageEnvelope",
    "ChatRequestEnvelope",
    "ChatToolCallEnvelope",
    "ChatToolCallFunctionEnvelope",
    "CheckoutSessionResponse",
    "ConfirmTotpEnrollmentRequest",
    "CreateAccountRequest",
    "CreateCheckoutSessionRequest",
    "CreateFirewallRequest",
    "CreateFirewallRuleRequest",
    "CreateInstanceRequest",
    "CreateInstanceRequestWorkloadKind",
    "CreateInvitationRequest",
    "CreateServingEndpointRequest",
    "CreateSmartBalancerRequest",
    "CreateTargetGroupRequest",
    "CreateVectorDatabaseRequest",
    "DebitBalanceRequest",
    "DebitBalanceResponse",
    "DebitOperationResponse",
    "DeleteFirewallResponse200",
    "DeleteFirewallRuleResponse200",
    "DeleteV1ResponsesSessionResponse200",
    "DeleteV1ResponsesSessionsResponse200",
    "DeleteVectorDatabaseResponse200",
    "DetectionStreamError",
    "DetectionStreamEvent",
    "DetectionStreamOptions",
    "DismissRequest",
    "DismissResponse",
    "EmbeddingsRequestEnvelope",
    "EnableSharedCapacityRequest",
    "ErrorResponse",
    "ExecutionDecisionChoiceAnswer",
    "ExecutionDecisionChoiceAnswerProbabilities",
    "ExecutionDecisionChoiceAnswerType",
    "ExecutionDecisionChoiceQuestion",
    "ExecutionDecisionChoiceQuestionCriteria",
    "ExecutionDecisionChoiceQuestionType",
    "ExecutionDecisionDiagnostics",
    "ExecutionDecisionNoulAnswer",
    "ExecutionDecisionNoulAnswerProbabilitiesType0",
    "ExecutionDecisionNoulAnswerProbabilitiesType1",
    "ExecutionDecisionNoulAnswerType",
    "ExecutionDecisionNoulQuestion",
    "ExecutionDecisionNoulQuestionCriteriaType0",
    "ExecutionDecisionNoulQuestionType",
    "ExecutionDecisionScoreAnswer",
    "ExecutionDecisionScoreAnswerLegend",
    "ExecutionDecisionScoreAnswerProbabilities",
    "ExecutionDecisionScoreAnswerType",
    "ExecutionDecisionScoreQuestion",
    "ExecutionDecisionScoreQuestionType",
    "ExecutionDecisionUsage",
    "ExecutionForecastInput",
    "ExecutionForecastPrediction",
    "ExecutionForecastRequest",
    "ExecutionForecastResponse",
    "ExecutionSystemOneRequest",
    "ExecutionSystemOneRequestQuestions",
    "ExecutionSystemOneRequestStateType1",
    "ExecutionSystemOneResponse",
    "ExecutionSystemOneResponseAnswers",
    "ExecutionSystemOneResponseDiagnostics",
    "FinishPasskeyloginRequest",
    "FinishPasskeyloginResponse",
    "FinishPasskeyRegistrationRequest",
    "FirewallEvaluationRequest",
    "FirewallEvaluationResponse",
    "FirewallResponse",
    "FirewallRuleEvaluationRequest",
    "FirewallRuleResponse",
    "ForgotPasswordRequest",
    "ForgotPasswordResponse",
    "GetAuthOauthIdentitiesResponse200",
    "GetInstanceUsageRange",
    "GetServingEndpointsResponse200",
    "GetSmartBalancersResponse200",
    "GetTargetGroupsResponse200",
    "GetTemplateBySlugResponse",
    "GetToolsResponse200",
    "GetUserVariantResponse",
    "GetV1AudioVoicesResponse200",
    "GetV1ModelsResponse200",
    "GetV1PublicTokenUsageResponse200",
    "GetV1PublicTokenUsageResponse200DaysItem",
    "GetV1PublicTokenUsageResponse200PeriodTotals",
    "GetV1PublicTokenUsageResponse200Totals",
    "GetV1ResponsesSessionDetailResponse200",
    "GetV1ResponsesSessionsListResponse200",
    "GetV1ResponsesSessionsStatusResponse200",
    "GpuListResponse",
    "GpuPreferenceResponse",
    "HttpTarget",
    "HttpTargetLabels",
    "HuggingFaceFileResponse",
    "HuggingFaceFilesResponse",
    "HuggingFaceGGUFFileResponse",
    "HuggingFaceModelResponse",
    "HuggingFaceModelsResponse",
    "HuggingFaceOrgInfoResponse",
    "HuggingFaceYOLOFileResponse",
    "ImageDetectionBoxOutput",
    "ImageDetectionKeypointOutput",
    "ImageDetectionOutput",
    "ImageDetectionResultOutput",
    "ImageGenerationRequest",
    "ImpersonationInfo",
    "IndexDocumentRequest",
    "IndexDocumentRequestMetadata",
    "IndexDocumentSourceRequest",
    "IndexDocumentsRequest",
    "IndexJobResponse",
    "InstanceListResponse",
    "InstanceResponse",
    "InstanceUsageBucketResponse",
    "InstanceUsageResponse",
    "InstanceUsageSummaryResponse",
    "InvitationListResponse",
    "InvitationResponse",
    "JoinSharedCapacityRequest",
    "LedgerEntryResponse",
    "LedgerHistoryResponse",
    "LegalAcceptanceItem",
    "LegalAcceptanceRequest",
    "ListDocumentsResponse",
    "ListedDocumentResponse",
    "ListedDocumentResponseMetadata",
    "ListNotificationsResponse",
    "ListUserVariantsResponse",
    "LoginRequest",
    "LoginResponse",
    "MarkAllReadRequest",
    "MarkAllReadResponse",
    "Model",
    "ModelPricesResponse",
    "NotificationLinkResponse",
    "NotificationLinkResponseRouteArgs",
    "NotificationResponse",
    "NotificationResponseBodyArgs",
    "NotificationResponseMetadata",
    "NotificationResponseTitleArgs",
    "OauthSignupRequest",
    "OauthTOTPRequest",
    "PasskeyListResponse",
    "PasskeyResponse",
    "PaymentResponse",
    "PaymentsResponse",
    "PostAuthOauthSignupResponse200",
    "PostAuthOauthTotpResponse200",
    "PostOllamaShowBody",
    "PostOllamaShowResponse200",
    "PostRuntimeNotifyCrashBody",
    "PostRuntimeNotifyProgressResponse200",
    "PostServingEndpointResponse409",
    "PostV1AudioTranscriptionsBody",
    "PostV1AudioTranscriptionsResponse200",
    "PostV1ChatCompletionsResponse200",
    "PostV1ChatCompletionsResponse403",
    "PostV1EmbeddingsResponse200",
    "PostV1ImageDetectionsBody",
    "PostV1ImageEditsBody",
    "PostV1ImageEditsResponse200",
    "PostV1ImageGenerationsResponse200",
    "PostV1ResponsesCompactResponse200",
    "PostV1ResponsesResponse200",
    "PostV1VideoGenerationsFilesBody",
    "PostV1VideoGenerationsFilesBodyAspectRatio",
    "PostV1VideoGenerationsFilesBodyFps",
    "PostV1VideoGenerationsFilesBodyTask",
    "PostV1VideoGenerationsJsonBody",
    "PostV1VideoGenerationsJsonBodyAspectRatio",
    "PostV1VideoGenerationsJsonBodyFps",
    "PostV1VideoGenerationsJsonBodyTask",
    "PostV1VideoJobFilesBody",
    "PostV1VideoJobFilesBodyAspectRatio",
    "PostV1VideoJobFilesBodyFps",
    "PostV1VideoJobFilesBodyTask",
    "PostV1VideoJobJsonBody",
    "PostV1VideoJobJsonBodyAspectRatio",
    "PostV1VideoJobJsonBodyFps",
    "PostV1VideoJobJsonBodyTask",
    "PostVectorDatabaseIndexDirectResponse200",
    "PostVectorDatabaseIndexJobsResponse202",
    "PostVectorDatabaseViewElementResponse200",
    "PreviewInstanceRequest",
    "PreviewInstanceRequestWorkloadKind",
    "PreviewInstanceResponse",
    "PreviewInstanceUpdateRequest",
    "PricingService",
    "PricingStatus",
    "ProtocolContextManagement",
    "PublicEndpointPriceResponse",
    "PublicEndpointResponse",
    "PublicEndpointsResponse",
    "PublicGPUPreferenceJSON",
    "PublicPricingAvailability",
    "PublicPricingGPU",
    "PublicPricingResponse",
    "PublicPricingService",
    "PublicTokenUsageDay",
    "PublicTokenUsageResponse",
    "PublicTokenUsageTotal",
    "PutV1ResponsesSessionsStatusBody",
    "PutV1ResponsesSessionsStatusResponse200",
    "QueuedDebitResponse",
    "RecommendedGPU",
    "RecommendRequest",
    "RefreshResponse",
    "RegisterPasskeyRequest",
    "RegisterRequest",
    "RegisterResponse",
    "ReplicaSetListResponse",
    "ReplicaSetResponse",
    "ResendActivationEmailRequest",
    "ResendEmailResponse",
    "ResendLoginEmailRequest",
    "ResetPasswordRequest",
    "ResetPasswordResponse",
    "ResourceMetricSnapshot",
    "ResourceMetricsResponse",
    "ResponsesRequestEnvelope",
    "ResponsesRequestEnvelopeMetadata",
    "ResponsesRequestEnvelopeReasoning",
    "RuntimeConfigRequest",
    "RuntimeConfigRequestStorageMountsItem",
    "RuntimeConfigResponse",
    "RuntimeConfigResponseStorageMountsItem",
    "RuntimeMemoryEstimateResponse",
    "RuntimeProgressRequest",
    "ScaleReplicaSetRequest",
    "ScheduleRuleListResponse",
    "ScheduleRuleRequest",
    "ScheduleRuleResponse",
    "SearchHitResponse",
    "SearchHitResponseMetadata",
    "SearchHitSourceResponse",
    "SearchRecommendRequest",
    "SearchRequest",
    "ServiceBiomolecularArtifact",
    "ServiceBiomolecularAttachment",
    "ServiceBiomolecularJobResult",
    "ServiceBiomolecularJobResultAffinity",
    "ServiceBiomolecularJobResultConfidenceItem",
    "ServiceBiomolecularJobResultMetadata",
    "ServiceBiomolecularOptions",
    "ServiceBiomolecularSubmitRequest",
    "ServiceBiomolecularSubmitRequestInput",
    "ServiceVideoJobContentURL",
    "ServiceVideoJobResult",
    "ServiceVideoJobResultStatus",
    "ServingEndpointResponse",
    "ServingProviderResponse",
    "ServingTargetRequest",
    "ServingTargetResponse",
    "SharedCapacityInstanceResponse",
    "SharedCapacityLinkResponse",
    "SharedCapacityListResponse",
    "SharedCapacityMembershipResponse",
    "SharedCapacityPublicListResponse",
    "SharedCapacityPublicResponse",
    "SharedCapacityResponse",
    "SmartBalancerRouteDestinationRequest",
    "SmartBalancerRouteDestinationResponse",
    "SmartBalancerRouteRequest",
    "SmartBalancerRouteResponse",
    "SmartBalancerRouterModelRequest",
    "SmartBalancerRouterModelResponse",
    "SmartBalancerViewResponse",
    "StartupProgress",
    "TargetGroupMemberRequest",
    "TargetGroupMemberResponse",
    "TargetGroupResponse",
    "Template",
    "TemplateWithVariants",
    "Timestamp",
    "Translation",
    "TryToolBody",
    "TryToolResponse200",
    "TutorialProgressResponse",
    "UnreadCountResponse",
    "UnreadCountResponseBySeverity",
    "UpdateAccountMemberRequest",
    "UpdateAccountRequest",
    "UpdateFirewallRequest",
    "UpdateFirewallRuleRequest",
    "UpdateInstanceRequest",
    "UpdatePreferencesRequest",
    "UpdateReplicaSetRequest",
    "UpdateSmartBalancerRequest",
    "UpdateTargetGroupRequest",
    "UpdateTutorialProgressRequest",
    "UpdateVectorDatabaseRequest",
    "UserInfoResponse",
    "UserPreferencesResponse",
    "Variant",
    "VariantTranslation",
    "VariantWithRelations",
    "VectorDatabaseResponse",
    "VerifyEmailResponse",
    "VideoJobsListResponse",
    "ViewElementRequest",
)
