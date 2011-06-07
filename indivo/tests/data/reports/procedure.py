from indivo.tests.data.base import TestXMLDoc

_TEST_PROCEDURES = [
    """
<Procedure xmlns='http://indivo.org/vocab/xml/documents#'>
  <datePerformed>2009-05-16T12:00:00Z</datePerformed>
  <name type='http://codes.indivo.org/procedures#' value='85' abbrev='append'>Appendectomy</name>
  <provider>
    <name>Kenneth Mandl</name>
    <institution>Children's Hospital Boston</institution>
  </provider>
</Procedure>
""",

    """
<Procedure xmlns='http://indivo.org/vocab/xml/documents#'>
  <datePerformed>2009-06-16T12:00:00Z</datePerformed>
  <name>Appendectomy</name>
  <provider>
    <name>Kenneth Mandl</name>
    <institution>Children's Hospital Boston</institution>
  </provider>
</Procedure>
""",
]

TEST_PROCEDURES = [TestXMLDoc(raw_content) for raw_content in _TEST_PROCEDURES]
