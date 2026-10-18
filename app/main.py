from app.cafe import Cafe


from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> None:
    count_of_visitors = 0
    mask_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            count_of_visitors += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_to_buy += 1
        else:
            if count_of_visitors == len(friends):
                return f"Friends can go to {cafe.name}"
    if mask_to_buy > 0:
        return f"Friends should buy {mask_to_buy} masks"
