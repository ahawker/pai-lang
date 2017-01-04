"""
    test_syntax
    ~~~~~~~~~~~

    Tests for the :mod:`~pai_lang.syntax` module.
"""

import pytest

from pai_lang import syntax


@pytest.fixture(scope='function')
def fake_root_node(fake_root_node_input):
    """
    Fixture that yields the result of :func:`~pai_lang.syntax.root` with fake values.
    """
    return syntax.root(*fake_root_node_input)


@pytest.fixture(scope='function')
def fake_child_node(fake_child_node_input, fake_root_node):
    """
    Fixture that yields the result of :func:`~pai_lang.syntax.child` with fake values and a root node generated by the
    :func:`fake_root_node` fixture.
    """
    return syntax.child(*fake_child_node_input, parent=fake_root_node)


def is_root_node(node):
    """
    Return `True` if the given node is a "root" node, `False` otherwise.
    """
    if not node:
        return False
    return node.is_root is True and node.is_child is False


def is_child_node(node):
    """
    Return `True` if the given node is a "child" node, `False` otherwise.
    """
    if not node:
        return False
    return node.is_child is True and node.is_root is False


def test_root_creates_root_node(fake_root_node):
    """
    Assert that :func:`~pai_lang.syntax.root` creates a :class:`~pai_lang.syntax.Node` instance whose
    :prop:`~pai_lang.syntax.Node.is_root` returns `True`.
    """
    assert isinstance(fake_root_node, syntax.Node)
    assert is_root_node(fake_root_node)


def test_root_creates_node_with_no_links(fake_root_node):
    """
    Assert that :func:`~pai_lang.syntax.root` creates a :class:`~pai_lang.syntax.Node` instance with no child links.
    """
    assert fake_root_node.child is None


def test_child_creates_child_node(fake_child_node):
    """
    Assert that :func:`~pai_lang.syntax.child` creates a :class:`~pai_lang.syntax.Node` instance whose
    :prop:`~pai_lang.syntax.Node.is_root` returns `False`.
    """
    assert isinstance(fake_child_node, syntax.Node)
    assert is_child_node(fake_child_node)


def test_child_creates_nodes_with_links(fake_child_node, fake_root_node):
    """
    Assert that :func:`~pai_lang.syntax.child` creates a :class:`~pai_lang.syntax.Node` instance with a parent link to the root
    node and the root node with links to the child.
    """
    assert fake_root_node.child == fake_child_node
    assert fake_child_node.parent == fake_root_node
