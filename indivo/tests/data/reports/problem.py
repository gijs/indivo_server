from indivo.tests.data.base import TestXMLDoc

_TEST_PROBLEMS = [
    """
<Problem xmlns='http://indivo.org/vocab/xml/documents#'>
  <dateOnset>2009-05-16T12:00:00Z</dateOnset>
  <dateResolution>2009-05-16T16:00:00Z</dateResolution>
  <name type='http://codes.indivo.org/problems/' value='123' abbrev='MI'>Myocardial Infarction</name>
  <comments>mild heart attack</comments>
  <diagnosedBy>Steve Zabak</diagnosedBy>
</Problem>
""",

    """
<Problem xmlns='http://indivo.org/vocab/xml/documents#'>
  <dateOnset>2009-05-16T12:00:00Z</dateOnset>
  <dateResolution>2009-05-16T16:00:00Z</dateResolution>
  <name>Myocardial Infarction</name>
  <comments>mild heart attack</comments>
  <diagnosedBy>Steve Zabak</diagnosedBy>
</Problem>
""",

    """
<Problem xmlns='http://indivo.org/vocab/xml/documents#'>
  <name>Myocardial Infarction</name>
  <comments>mild heart attack</comments>
  <diagnosedBy>Steve Zabak</diagnosedBy>
</Problem>
""",
]

TEST_PROBLEMS = [TestXMLDoc(raw_content) for raw_content in _TEST_PROBLEMS]

