from typing import Any

from pydantic import Field
from datetime import datetime
from enum import Enum, StrEnum

from pydantic import BaseModel
from fastapi.params import Query

PAYMENT_SUCCESS_STATUS = 0


class SumBillsByIdSchema(BaseModel):
    plate: str
    amount: int


class _GatewayTypes(str, Enum):
    pos = "pos"
    wspos = "wspos"
    ipg = "ipg"
    mock = "mock"


class _Providers(StrEnum):
    parsian = "parsian"
    internal = "internal"
    rayanpay = "rayanpay"


class BillPaymentSchemaPOS(BaseModel):
    bill_ids: list[int]
    serial_number: str | None = None


class BillPaymentSchemaIPG(BaseModel):
    bill_ids: list[int]
    phone_number: str | None = None
    call_back: str | None = None


class _PaymentStatus(str, Enum):
    Verified = "Verified"  # Payment was verified and is considered successful
    Failed = "Failed"  # The payment was not successful
    SentToPos = "SentToPos"  # The payment has just been Sent To Pos


class PaymentReportInput(BaseModel):
    mobile: str | None = None
    order_id: int | None = None
    from_date: datetime | None = None
    to_date: datetime | None = None
    reference_number: str | None = None
    gateway: _GatewayTypes | None = None
    is_government: bool | None = None
    terminal: str | None = None
    token: str | None = None
    provider_status: int | None = None
    amount: int | None = None
    min_amount: int | None = None
    max_amount: int | None = None
    services: list[str] | None = Field(Query(None))
    status: list[_PaymentStatus] | None = Field(Query(None))
    has_refund: bool | None = None


class MakePaymentResponse(BaseModel):
    order_id: int
    token: str
    amount: int
    amount_in_currency: int
    currency: str
    url: str | None = None


class VerifyPaymentRequest(BaseModel):
    order_id: int
    username: str = ""
    password: str = ""


class TransactionUpdate(BaseModel):
    order_id: int | None = None


class TransactionCreate(BaseModel):
    bill_ids: list[int] | None = None
    order_id: int | None = None
    amount: int | None = None
    callback_url: str | None = None


class MakePaymentRequest(BaseModel):
    gateway: _GatewayTypes = _GatewayTypes.wspos
    provider: _Providers = _Providers.internal
    amount: int
    terminal: str
    username: str = ""
    password: str = ""
    additional_data: dict | str = ""
    mobile: str | None = None
    service: str | None = "pms"
    iban_list: list[dict[str, Any]] = []
    iban: str | None = None
    govid: str | None = None
    card_token: str | None = None
    callback_url: str | None = None
    is_government: bool = False


class PaymentUrlEndpoint(StrEnum):
    make = "/payment/make"
    verify = "/payment/verify"
    reports = "/reports/"
    reports_log = "/reports/logs"


class VerifyPaymentResponse(BaseModel):
    status: _PaymentStatus
    amount: int
    reference_number: str | None = None
    verified_at: datetime | None = None
