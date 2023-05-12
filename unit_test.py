    @action(detail=True, methods=["post"], url_path="claim-profile")
    def claim_profile(self, request: Request, pk: str) -> Response:
        seafarer_usecases.claim_profile(pk, request.user.user_id)
        return EmptyResponse()
