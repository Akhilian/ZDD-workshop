from business.entities.Identifier import Identifier


class IdentifierTest():
    def test_should_have_a_representation(self):
        assert repr(Identifier('1')) == '1'
