from dataclasses import dataclass

@dataclass
class PlaceTypes:
    car_dealer: str = 'car_dealer'
    car_rental: str = 'car_rental'
    car_repair: str = 'car_repair'
    car_wash: str = 'car_wash'
    electric_vehicle_charging_station: str = 'electric_vehicle_charging_station'
    gas_station: str = 'gas_station'
    parking: str = 'parking'
    rest_stop: str = 'rest_stop'
    farm: str = 'farm'
    art_gallery: str = 'art_gallery'
    museum: str = 'museum'
    performing_arts_theater: str = 'performing_arts_theater'
    library: str = 'library'
    preschool: str = 'preschool'
    primary_school: str = 'primary_school'
    school: str = 'school'
    secondary_school: str = 'secondary_school'
    university: str = 'university'
    amusement_center: str = 'amusement_center'
    amusement_park: str = 'amusement_park'
    aquarium: str = 'aquarium'
    banquet_hall: str = 'banquet_hall'
    bowling_alley: str = 'bowling_alley'
    casino: str = 'casino'
    community_center: str = 'community_center'
    convention_center: str = 'convention_center'
    cultural_center: str = 'cultural_center'
    dog_park: str = 'dog_park'
    event_venue: str = 'event_venue'
    hiking_area: str = 'hiking_area'
    historical_landmark: str = 'historical_landmark'
    marina: str = 'marina'
    movie_rental: str = 'movie_rental'
    movie_theater: str = 'movie_theater'
    national_park: str = 'national_park'
    night_club: str = 'night_club'
    park: str = 'park'
    tourist_attraction: str = 'tourist_attraction'
    visitor_center: str = 'visitor_center'
    wedding_venue: str = 'wedding_venue'
    zoo: str = 'zoo'
    accounting: str = 'accounting'
    atm: str = 'atm'
    bank: str = 'bank'
    american_restaurant: str = 'american_restaurant'
    bakery: str = 'bakery'
    bar: str = 'bar'
    barbecue_restaurant: str = 'barbecue_restaurant'
    brazilian_restaurant: str = 'brazilian_restaurant'
    breakfast_restaurant: str = 'breakfast_restaurant'
    brunch_restaurant: str = 'brunch_restaurant'
    cafe: str = 'cafe'
    chinese_restaurant: str = 'chinese_restaurant'
    coffee_shop: str = 'coffee_shop'
    fast_food_restaurant: str = 'fast_food_restaurant'
    french_restaurant: str = 'french_restaurant'
    greek_restaurant: str = 'greek_restaurant'
    hamburger_restaurant: str = 'hamburger_restaurant'
    ice_cream_shop: str = 'ice_cream_shop'
    indian_restaurant: str = 'indian_restaurant'
    indonesian_restaurant: str = 'indonesian_restaurant'
    italian_restaurant: str = 'italian_restaurant'
    japanese_restaurant: str = 'japanese_restaurant'
    korean_restaurant: str = 'korean_restaurant'
    lebanese_restaurant: str = 'lebanese_restaurant'
    meal_delivery: str = 'meal_delivery'
    meal_takeaway: str = 'meal_takeaway'
    mediterranean_restaurant: str = 'mediterranean_restaurant'
    mexican_restaurant: str = 'mexican_restaurant'
    middle_eastern_restaurant: str = 'middle_eastern_restaurant'
    pizza_restaurant: str = 'pizza_restaurant'
    ramen_restaurant: str = 'ramen_restaurant'
    restaurant: str = 'restaurant'
    sandwich_shop: str = 'sandwich_shop'
    seafood_restaurant: str = 'seafood_restaurant'
    spanish_restaurant: str = 'spanish_restaurant'
    steak_house: str = 'steak_house'
    sushi_restaurant: str = 'sushi_restaurant'
    thai_restaurant: str = 'thai_restaurant'
    turkish_restaurant: str = 'turkish_restaurant'
    vegan_restaurant: str = 'vegan_restaurant'
    vegetarian_restaurant: str = 'vegetarian_restaurant'
    vietnamese_restaurant: str = 'vietnamese_restaurant'
    administrative_area_level_1: str = 'administrative_area_level_1'
    administrative_area_level_2: str = 'administrative_area_level_2'
    country: str = 'country'
    locality: str = 'locality'
    postal_code: str = 'postal_code'
    school_district: str = 'school_district'
    city_hall: str = 'city_hall'
    courthouse: str = 'courthouse'
    embassy: str = 'embassy'
    fire_station: str = 'fire_station'
    local_government_office: str = 'local_government_office'
    police: str = 'police'
    post_office: str = 'post_office'
    dental_clinic: str = 'dental_clinic'
    dentist: str = 'dentist'
    doctor: str = 'doctor'
    drugstore: str = 'drugstore'
    hospital: str = 'hospital'
    medical_lab: str = 'medical_lab'
    pharmacy: str = 'pharmacy'
    physiotherapist: str = 'physiotherapist'
    spa: str = 'spa'
    bed_and_breakfast: str = 'bed_and_breakfast'
    campground: str = 'campground'
    camping_cabin: str = 'camping_cabin'
    cottage: str = 'cottage'
    extended_stay_hotel: str = 'extended_stay_hotel'
    farmstay: str = 'farmstay'
    guest_house: str = 'guest_house'
    hostel: str = 'hostel'
    hotel: str = 'hotel'
    lodging: str = 'lodging'
    motel: str = 'motel'
    private_guest_room: str = 'private_guest_room'
    resort_hotel: str = 'resort_hotel'
    rv_park: str = 'rv_park'
    church: str = 'church'
    hindu_temple: str = 'hindu_temple'
    mosque: str = 'mosque'
    synagogue: str = 'synagogue'
    barber_shop: str = 'barber_shop'
    beauty_salon: str = 'beauty_salon'
    cemetery: str = 'cemetery'
    child_care_agency: str = 'child_care_agency'
    consultant: str = 'consultant'
    courier_service: str = 'courier_service'
    electrician: str = 'electrician'
    florist: str = 'florist'
    funeral_home: str = 'funeral_home'
    hair_care: str = 'hair_care'
    hair_salon: str = 'hair_salon'
    insurance_agency: str = 'insurance_agency'
    laundry: str = 'laundry'
    lawyer: str = 'lawyer'
    locksmith: str = 'locksmith'
    moving_company: str = 'moving_company'
    painter: str = 'painter'
    plumber: str = 'plumber'
    real_estate_agency: str = 'real_estate_agency'
    roofing_contractor: str = 'roofing_contractor'
    storage: str = 'storage'
    tailor: str = 'tailor'
    telecommunications_service_provider: str = 'telecommunications_service_provider'
    travel_agency: str = 'travel_agency'
    veterinary_care: str = 'veterinary_care'
    auto_parts_store: str = 'auto_parts_store'
    bicycle_store: str = 'bicycle_store'
    book_store: str = 'book_store'
    cell_phone_store: str = 'cell_phone_store'
    clothing_store: str = 'clothing_store'
    convenience_store: str = 'convenience_store'
    department_store: str = 'department_store'
    discount_store: str = 'discount_store'
    electronics_store: str = 'electronics_store'
    furniture_store: str = 'furniture_store'
    gift_shop: str = 'gift_shop'
    grocery_store: str = 'grocery_store'
    hardware_store: str = 'hardware_store'
    home_goods_store: str = 'home_goods_store'
    home_improvement_store: str = 'home_improvement_store'
    jewelry_store: str = 'jewelry_store'
    liquor_store: str = 'liquor_store'
    market: str = 'market'
    pet_store: str = 'pet_store'
    shoe_store: str = 'shoe_store'
    shopping_mall: str = 'shopping_mall'
    sporting_goods_store: str = 'sporting_goods_store'
    store: str = 'store'
    supermarket: str = 'supermarket'
    wholesaler: str = 'wholesaler'
    athletic_field: str = 'athletic_field'
    fitness_center: str = 'fitness_center'
    golf_course: str = 'golf_course'
    gym: str = 'gym'
    playground: str = 'playground'
    ski_resort: str = 'ski_resort'
    sports_club: str = 'sports_club'
    sports_complex: str = 'sports_complex'
    stadium: str = 'stadium'
    swimming_pool: str = 'swimming_pool'
    airport: str = 'airport'
    bus_station: str = 'bus_station'
    bus_stop: str = 'bus_stop'
    ferry_terminal: str = 'ferry_terminal'
    heliport: str = 'heliport'
    light_rail_station: str = 'light_rail_station'
    park_and_ride: str = 'park_and_ride'