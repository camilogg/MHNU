from import_export import widgets, fields
from import_export.resources import ModelResource

from museum.models import Record
from museum.utils import snake_case_to_camel_case


class RecordModelResource(ModelResource):
    country = fields.Field(
        attribute='locality__municipality__county__state_province__country__name',
        column_name='country',
        readonly=True
    )
    country_code = fields.Field(
        attribute='locality__municipality__county__state_province__country__country_code',
        column_name='countryCode',
        readonly=True
    )
    state_province = fields.Field(
        attribute='locality__municipality__county__state_province__name',
        column_name='stateProvince',
        readonly=True
    )
    county = fields.Field(
        attribute='locality__municipality__county__name',
        column_name='county',
        readonly=True
    )
    municipality = fields.Field(
        attribute='locality__municipality__name',
        column_name='municipality',
        readonly=True
    )
    verbatim_locality = fields.Field(
        attribute='locality__verbatim_locality',
        column_name='verbatimLocality',
        readonly=True
    )

    class Meta:
        model = Record
        exclude = []
        # import_id_fields = ['occurrence_ID']
        export_order = (
            'id', 'occurrence_ID', 'basis_of_record', 'institution_code',
            'collection_code', 'catalog_number', 'type', 'modified',
            'language', 'license', 'rights_holder', 'access_rights',
            'bibliographic_citation', 'references', 'institution_ID',
            'collection_ID', 'dataset_ID', 'dataset_name',
            'owner_institution_code', 'information_withheld',
            'data_generalizations', 'dynamic_properties', 'occurrence_remarks',
            'record_number', 'recorded_by', 'organism_ID', 'individual_count',
            'organism_quantity', 'organism_quantity_type', 'organism_name',
            'organism_scope', 'associated_organisms', 'organism_remarks',
            'sex', 'life_stage', 'reproductive_condition', 'behavior',
            'establishment_means', 'occurrence_status', 'preparations',
            'disposition', 'other_catalog_numbers', 'previous_identifications',
            'associated_media', 'associated_references',
            'associated_occurrences', 'associated_sequences',
            'associated_taxa', 'material_sample_ID', 'parent_event_ID',
            'event_ID', 'sampling_protocol', 'sampling_size_value',
            'sampling_size_unit', 'sampling_effort', 'event_date',
            'event_time', 'start_day_of_year', 'end_day_of_year', 'year',
            'month', 'day', 'verbatim_event_date', 'habitat', 'field_number',
            'field_notes', 'event_remarks', 'location_ID',
            'higher_geography_ID', 'higher_geography', 'continent',
            'water_body', 'island_group', 'island', 'country', 'country_code',
            'state_province', 'county', 'municipality', 'locality',
            'verbatim_locality', 'verbatim_elevation',
            'minimum_elevation_in_meters', 'maximum_elevation_in_meters',
            'verbatim_depth', 'minimum_depth_in_meters',
            'maximum_depth_in_meters',
            'minimum_distance_above_surface_in_meters',
            'maximum_distance_above_surface_in_meters',
            'location_according_to', 'location_remarks',
            'verbatim_coordinates', 'verbatim_latitude', 'verbatim_longitude',
            'verbatim_coordinate_system', 'verbatim_SRS', 'decimal_latitude',
            'decimal_longitude', 'geodetic_datum',
            'coordinate_uncertainty_in_meters', 'coordinate_precision',
            'point_radius_spatial_fit', 'footprint_WKT', 'footprint_SRS',
            'footprint_spatial_fit', 'georeferenced_by', 'georeferenced_date',
            'georeference_protocol', 'georeference_sources',
            'georeference_verification_status', 'georeference_remarks',
            'geological_context_ID', 'earliest_eon_or_lowest_eonothem',
            'latest_eon_or_highest_eonothem', 'earliest_era_or_lowest_erathem',
            'latest_era_or_highest_erathem',
            'earliest_period_or_lowest_system',
            'latest_period_or_highest_system',
            'earliest_epoch_or_lowest_series',
            'latest_epoch_or_highest_series', 'earliest_age_or_lowest_stage',
            'latest_age_or_highest_stage', 'lowest_biostratigraphic_zone',
            'highest_biostratigraphic_zone', 'lithostratigraphic_terms',
            'group', 'formation', 'member', 'bed', 'identification_ID',
            'identified_by', 'date_identified', 'identification_references',
            'identification_verification_status', 'identification_remarks',
            'identification_qualifier', 'type_status', 'taxon_ID',
            'scientific_name_ID', 'accepted_name_usage_ID',
            'parent_name_usage_ID', 'original_name_usage_ID',
            'name_according_to_ID', 'name_published_in_ID', 'taxon_concept_ID',
            'scientific_name', 'accepted_name_usage', 'parent_name_usage',
            'original_name_usage', 'name_according_to', 'name_published_in',
            'name_published_in_year', 'higher_classification', 'kingdom',
            'phylum', '_class', 'order', 'family', 'genus', 'subgenus',
            'specific_epithet', 'infraspecific_epithet', 'taxon_rank',
            'verbatim_taxon_rank', 'scientific_name_authorship',
            'vernacular_name', 'nomenclatural_code', 'taxonomic_status',
            'nomenclatural_status', 'taxon_remarks'
        )
        widgets = {
            'basis_of_record': {'field': 'name'},
            'type': {'field': 'name'},
            'collection_code': {'field': 'name'},
            'recorded_by': {'field': 'name'},
            'sex': {'field': 'name'},
            'life_stage': {'field': 'name'},
            'occurrence_status': {'field': 'name'},
            'preparations': {'field': 'name'},
            'disposition': {'field': 'name'},
            'sampling_protocol': {'field': 'name'},
            'habitat': {'field': 'name'},
            'water_body': {'field': 'name'},
            'locality': {'field': 'name'},
            'identified_by': {'field': 'name'},
            'scientific_name': {'field': 'name'},
            'kingdom': {'field': 'name'},
            'phylum': {'field': 'name'},
            '_class': {'field': 'name'},
            'order': {'field': 'name'},
            'family': {'field': 'name'},
            'genus': {'field': 'name'},
            'specific_epithet': {'field': 'name'},
            'taxon_rank': {'field': 'name'},
            'scientific_name_authorship': {'field': 'name'},
            'vernacular_name': {'field': 'name'},
            'nomenclatural_code': {'field': 'name'},
            'taxonomic_status': {'field': 'name'},
        }
        skip_unchanged = True
        clean_model_instances = True

    @classmethod
    def field_from_django_field(cls, field_name, django_field, readonly):
        """
        Returns a Resource Field instance for the given Django model field.
        """
        FieldWidget = cls.widget_from_django_field(django_field)
        widget_kwargs = cls.widget_kwargs_for_field(field_name)
        field = cls.DEFAULT_RESOURCE_FIELD(
            attribute=field_name,
            column_name=snake_case_to_camel_case(field_name),
            widget=FieldWidget(**widget_kwargs),
            readonly=readonly,
            default=django_field.default,
        )
        return field