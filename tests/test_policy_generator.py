import unittest
from src.utils.policy_generator import PolicyGenerator

class TestPolicyGenerator(unittest.TestCase):
    def test_generate_policy(self):
        # Example data
        all_permissions = ["permission1", "permission2", "permission3"]
        unused_permissions = {"permission3"}

        # Call the method
        updated_policy = PolicyGenerator.generate_policy(all_permissions, unused_permissions)

        # Assertions
        self.assertNotIn("permission3", updated_policy)
        self.assertIn("permission1", updated_policy)
        self.assertIn("permission2", updated_policy)
        self.assertEqual(len(updated_policy), 2)

    def test_generate_policy_empty_unused(self):
        # Example data
        all_permissions = ["permission1", "permission2", "permission3"]
        unused_permissions = set()

        # Call the method
        updated_policy = PolicyGenerator.generate_policy(all_permissions, unused_permissions)

        # Assertions
        self.assertEqual(set(updated_policy), set(all_permissions))

    def test_generate_policy_empty_permissions(self):
        # Example data
        all_permissions = []
        unused_permissions = {"permission3"}

        # Call the method
        updated_policy = PolicyGenerator.generate_policy(all_permissions, unused_permissions)

        # Assertions
        self.assertEqual(updated_policy, [])

    def test_invalid_inputs(self):
        # Invalid data
        with self.assertRaises(TypeError):
            PolicyGenerator.generate_policy("not_a_list", {"permission1"})

if __name__ == "__main__":
    unittest.main()
