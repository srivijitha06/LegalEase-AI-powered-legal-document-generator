from pydantic import BaseModel, Field


class DocumentRequest(BaseModel):
    document_type: str = Field(
        ...,
        min_length=2,
        max_length=200,
    )

    parties: str = Field(
        ...,
        min_length=2,
        max_length=5000,
    )

    terms: str = Field(
        ...,
        min_length=2,
        max_length=15000,
    )

    effective_date: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )

    jurisdiction: str = Field(
        default="Not specified",
        max_length=200,
    )

    language: str = Field(
        default="English",
        max_length=100,
    )


class AnalyzeRequest(BaseModel):
    document: str = Field(
        ...,
        min_length=20,
        max_length=30000,
    )


class RewriteRequest(BaseModel):
    document: str = Field(
        ...,
        min_length=20,
        max_length=30000,
    )

    instruction: str = Field(
        ...,
        min_length=2,
        max_length=2000,
    )