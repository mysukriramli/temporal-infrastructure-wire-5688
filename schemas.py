from datetime import timezone as dt_timezone
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field

class HealthResponse(BaseModel):
    status: str = Field(default='healthy', description='Operational health status')
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat(), description='UTC ISO-8601 timestamp')

class ToolItem(BaseModel):
    name: str = Field(..., description='Tool name')
    description: str = Field(..., description='Tool description')
    parameters: Dict[str, Any] = Field(default_factory=dict, description='Tool parameter schema')

class ToolsResponse(BaseModel):
    tools: List[Dict[str, Any]] = Field(default_factory=list, description='List of available tools')

class TemporalInfrastructureRequest(BaseModel):
    target_identifier: str = Field(default='global_time', description='Target timing infrastructure identifier')
    query_parameter: str = Field(default='temporal_analysis', description='Query type or focus parameter')
    lat: float = Field(default=2.27, description='Latitude coordinate clamped to [-90, 90]')
    lon: float = Field(default=102.55, description='Longitude coordinate clamped to [-180, 180]')
    window_steps: int = Field(default=24, description='Lookback or forecasting window steps')
    lookback_hours: int = Field(default=72, description='Analysis lookback duration in hours')
    resolution: int = Field(default=7, description='Spatial H3 resolution index [4, 9]')

class ExplainabilityWeights(BaseModel):
    synchronization: float = Field(default=0.4, description='Synchronization weight')
    clock_health: float = Field(default=0.3, description='Clock health weight')
    resilience: float = Field(default=0.2, description='Resilience weight')
    coordination: float = Field(default=0.1, description='Coordination weight')

class ExplainabilityDetail(BaseModel):
    primary_driver: str = Field(default='synchronization_integrity', description='Primary driver of temporal state')
    weights: ExplainabilityWeights = Field(default_factory=ExplainabilityWeights, description='Metric contribution weights')

class TemporalInfrastructureResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat(), description='UTC ISO-8601 timestamp')
    status: str = Field(default='healthy', description='Operational status descriptor')
    primary_metric: float = Field(default=97.3, description='Temporal Infrastructure Score (TIS)')
    secondary_score: float = Field(default=0.99, description='Secondary coordination index')
    state_index: float = Field(default=95.1, description='Synthesized state operational index')
    classification: str = Field(default='PRECISE', description='Synchronization / operational classification')
    explainability: ExplainabilityDetail = Field(default_factory=ExplainabilityDetail, description='Explainable metrics breakdown')

class SpatialH3TensorRequest(BaseModel):
    lat: float = Field(default=2.0442, description='Latitude coordinate clamped to [-90, 90]')
    lon: float = Field(default=102.5689, description='Longitude coordinate clamped to [-180, 180]')
    resolution: int = Field(default=7, description='Uber H3 spatial resolution [4, 9]')

class SpatialH3TensorResponse(BaseModel):
    h3_index: str = Field(default='876520d81ffffff', description='Hexagonal H3 spatial cell index')
    spatial_cell: str = Field(default='876520d81ffffff', description='Target spatial cell identifier')
    density_score: float = Field(default=93.1, description='Timing reference density score')
    terrain_state_index: float = Field(default=97.4, description='Spatial synchronization terrain index')
    status: str = Field(default='ACTIVE', description='Spatial grid node status')

class GenericTimingRequest(BaseModel):
    target_identifier: str = Field(default='global_time', description='Target system or node')
    lat: float = Field(default=2.27, description='Latitude coordinate')
    lon: float = Field(default=102.55, description='Longitude coordinate')
    lookback_hours: int = Field(default=72, description='Lookback window in hours')
    resolution: int = Field(default=7, description='H3 spatial resolution')

class GenericTimingResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat(), description='UTC ISO-8601 timestamp')
    status: str = Field(default='success', description='Execution status')
    metric_value: float = Field(default=95.0, description='Computed primary metric value')
    state: str = Field(default='PRECISE', description='State classification')
    details: Dict[str, Any] = Field(default_factory=dict, description='Detailed computational sub-metrics')