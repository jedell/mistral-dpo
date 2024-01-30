from dataclasses import dataclass

@dataclass
class Fields:
    # Basic Fields
    accessibilityOptions: str = 'places.accessibilityOptions'
    addressComponents: str = 'places.addressComponents'
    adrFormatAddress: str = 'places.adrFormatAddress'
    businessStatus: str = 'places.businessStatus'
    displayName: str = 'places.displayName'
    formattedAddress: str = 'places.formattedAddress'
    googleMapsUri: str = 'places.googleMapsUri'
    iconBackgroundColor: str = 'places.iconBackgroundColor'
    iconMaskBaseUri: str = 'places.iconMaskBaseUri'
    id: str = 'places.id'
    location: str = 'places.location'
    name: str = 'places.name'
    photos: str = 'places.photos'
    plusCode: str = 'places.plusCode'
    primaryType: str = 'places.primaryType'
    primaryTypeDisplayName: str = 'places.primaryTypeDisplayName'
    shortFormattedAddress: str = 'places.shortFormattedAddress'
    subDestinations: str = 'places.subDestinations'
    types: str = 'places.types'
    utcOffsetMinutes: str = 'places.utcOffsetMinutes'
    viewport: str = 'places.viewport'

    # Advanced Fields
    currentOpeningHours: str = 'places.currentOpeningHours'
    currentSecondaryOpeningHours: str = 'places.currentSecondaryOpeningHours'
    internationalPhoneNumber: str = 'places.internationalPhoneNumber'
    nationalPhoneNumber: str = 'places.nationalPhoneNumber'
    priceLevel: str = 'places.priceLevel'
    rating: str = 'places.rating'
    regularOpeningHours: str = 'places.regularOpeningHours'
    regularSecondaryOpeningHours: str = 'places.regularSecondaryOpeningHours'
    userRatingCount: str = 'places.userRatingCount'
    websiteUri: str = 'places.websiteUri'

    # Preferred Fields
    allowsDogs: str = 'places.allowsDogs'
    curbsidePickup: str = 'places.curbsidePickup'
    delivery: str = 'places.delivery'
    dineIn: str = 'places.dineIn'
    editorialSummary: str = 'places.editorialSummary'
    evChargeOptions: str = 'places.evChargeOptions'
    fuelOptions: str = 'places.fuelOptions'
    goodForChildren: str = 'places.goodForChildren'
    goodForGroups: str = 'places.goodForGroups'
    goodForWatchingSports: str = 'places.goodForWatchingSports'
    liveMusic: str = 'places.liveMusic'
    menuForChildren: str = 'places.menuForChildren'
    parkingOptions: str = 'places.parkingOptions'
    paymentOptions: str = 'places.paymentOptions'
    outdoorSeating: str = 'places.outdoorSeating'
    reservable: str = 'places.reservable'
    restroom: str = 'places.restroom'
    reviews: str = 'places.reviews'
    servesBeer: str = 'places.servesBeer'
    servesBreakfast: str = 'places.servesBreakfast'
    servesBrunch: str = 'places.servesBrunch'
    servesCocktails: str = 'places.servesCocktails'
    servesCoffee: str = 'places.servesCoffee'
    servesDesserts: str = 'places.servesDesserts'
    servesDinner: str = 'places.servesDinner'
    servesLunch: str = 'places.servesLunch'
    servesVegetarianFood: str = 'places.servesVegetarianFood'
    servesWine: str = 'places.servesWine'
    takeout: str = 'places.takeout'

    @staticmethod
    def parse_field(field_str: str) -> str:
        """
        Parses a string into the correct dataclass attribute.
        
        Args:
            field_str (str): The string representation of the field.
            
        Returns:
            str: The dataclass attribute corresponding to the input string.
        """
        field_mapping = {
            # Basic Fields
            'places.accessibilityOptions': Fields.accessibilityOptions,
            'places.addressComponents': Fields.addressComponents,
            'places.adrFormatAddress': Fields.adrFormatAddress,
            'places.businessStatus': Fields.businessStatus,
            'places.displayName': Fields.displayName,
            'places.formattedAddress': Fields.formattedAddress,
            'places.googleMapsUri': Fields.googleMapsUri,
            'places.iconBackgroundColor': Fields.iconBackgroundColor,
            'places.iconMaskBaseUri': Fields.iconMaskBaseUri,
            'places.id': Fields.id,
            'places.location': Fields.location,
            'places.name': Fields.name,
            'places.photos': Fields.photos,
            'places.plusCode': Fields.plusCode,
            'places.primaryType': Fields.primaryType,
            'places.primaryTypeDisplayName': Fields.primaryTypeDisplayName,
            'places.shortFormattedAddress': Fields.shortFormattedAddress,
            'places.subDestinations': Fields.subDestinations,
            'places.types': Fields.types,
            'places.utcOffsetMinutes': Fields.utcOffsetMinutes,
            'places.viewport': Fields.viewport,
            # Advanced Fields
            'places.currentOpeningHours': Fields.currentOpeningHours,
            'places.currentSecondaryOpeningHours': Fields.currentSecondaryOpeningHours,
            'places.internationalPhoneNumber': Fields.internationalPhoneNumber,
            'places.nationalPhoneNumber': Fields.nationalPhoneNumber,
            'places.priceLevel': Fields.priceLevel,
            'places.rating': Fields.rating,
            'places.regularOpeningHours': Fields.regularOpeningHours,
            'places.regularSecondaryOpeningHours': Fields.regularSecondaryOpeningHours,
            'places.userRatingCount': Fields.userRatingCount,
            'places.websiteUri': Fields.websiteUri,
            # Preferred Fields
            'places.allowsDogs': Fields.allowsDogs,
            'places.curbsidePickup': Fields.curbsidePickup,
            'places.delivery': Fields.delivery,
            'places.dineIn': Fields.dineIn,
            'places.editorialSummary': Fields.editorialSummary,
            'places.evChargeOptions': Fields.evChargeOptions,
            'places.fuelOptions': Fields.fuelOptions,
            'places.goodForChildren': Fields.goodForChildren,
            'places.goodForGroups': Fields.goodForGroups,
            'places.goodForWatchingSports': Fields.goodForWatchingSports,
            'places.liveMusic': Fields.liveMusic,
            'places.menuForChildren': Fields.menuForChildren,
            'places.parkingOptions': Fields.parkingOptions,
            'places.paymentOptions': Fields.paymentOptions,
            'places.outdoorSeating': Fields.outdoorSeating,
            'places.reservable': Fields.reservable,
            'places.restroom': Fields.restroom,
            'places.reviews': Fields.reviews,
            'places.servesBeer': Fields.servesBeer,
            'places.servesBreakfast': Fields.servesBreakfast,
            'places.servesBrunch': Fields.servesBrunch,
            'places.servesCocktails': Fields.servesCocktails,
            'places.servesCoffee': Fields.servesCoffee,
            'places.servesDesserts': Fields.servesDesserts,
            'places.servesDinner': Fields.servesDinner,
            'places.servesLunch': Fields.servesLunch,
            'places.servesVegetarianFood': Fields.servesVegetarianFood,
            'places.servesWine': Fields.servesWine,
            'places.takeout': Fields.takeout,
        }
        return field_mapping.get(field_str, "Unknown Field")