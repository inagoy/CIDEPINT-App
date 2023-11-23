"""Institution seeds."""
from src.core.models.institution import Institution


def seed_institutions() -> None:
    """
    Seed institutions in the database with initial data.

    This function populates the database with initial institution data
    for testing and development purposes.
    """
    institutions_data = [
        {"name": "Centro de Investigación en Pinturas Avanzadas",
         "info": "Centro líder en tecnología de pinturas",
         "address": "Av. Tecnología 1234",
         "location": "Buenos Aires",
         "coordinates": "{\"lat\":-34.72863401788879, \"lng\":-58.26324462890626}",
         "website": "www.centropinturas.com",
         "search_keywords":
            "investigación, desarrollo, tecnología, pinturas, Buenos Aires",
         "days_and_hours": "Lun-Vie: 9am-5pm",
         "contact_info": "info@centropinturas.com", "enabled": True},

        {"name": "Laboratorio de Pinturas Innovadoras",
         "info": "Laboratorio especializado en pinturas avanzadas",
         "address": "Calle Innovación 567",
         "location": "Córdoba",
         "coordinates": "{\"lat\":-34.92123209151683,\"lng\":-57.95451164245606}",
         "website": "www.labpinturas.com",
         "search_keywords": "laboratorio, innovación, pinturas, Córdoba",
         "days_and_hours": "Lun-Vie: 8:30am-4:30pm",
         "contact_info": "info@labpinturas.com", "enabled": True},
        {
         "name": "Centro de Desarrollo en Pinturas Sustentables",
         "info": "Centro dedicado al desarrollo de pinturas ecológicas y sostenibles",
         "address": "Ruta Sustentabilidad 789", "location": "Rosario",
         "website": "www.cidepintsustentables.com",
         "search_keywords": "desarrollo, pinturas, sustentables, Rosario",
         "days_and_hours": "Lun-Vie: 9:30am-5:30pm",
         "contact_info": "info@cidepintsustentables.com", "enabled": True
        }
    ]

    for institution_data in institutions_data:
        institution = Institution.save(**institution_data)
        print(f"""Created institution: {institution.name} - Info: {
            institution.info}""")
