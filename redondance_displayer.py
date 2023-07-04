import gym
import imageio
import matplotlib.pyplot as plt

# Create the CartPole environment
env = gym.make('CartPole-v1')

# Set the number of episodes to run
num_episodes = 2

for episode in range(num_episodes):
    observation = env.reset()  # Reset the environment for a new episode
    episode_reward = 0  # Track the cumulative reward for the episode

    frames = []  # List to store frames for the GIF

    action_count = 1  # Initialize the action count for the current episode

    while True:
        frames.append(env.render(mode='rgb_array'))  # Capture the frame (mode='rgb_array')

        # Choose a random action
        action = env.action_space.sample()

        # Perform the action and observe the next state, reward, and done flag
        next_observation, reward, done, _ = env.step(action)

        episode_reward += reward  # Accumulate the reward

        if action_count % 5 == 0:
            print(f'Episode {episode+1}, Action {action_count}: obs: s1: {next_observation[0]}, s2: {next_observation[1]}, s3: {next_observation[2]}, s4: {next_observation[3]}')
            print(f"Episode {episode+1}, Action: {action}")

            # Create a plot to display the states
            plt.figure(dpi=300)
            plt.plot(next_observation)
            plt.xlabel('State Index')
            plt.ylabel('State Value')
            plt.title(f'Episode {episode+1}, Action {action_count}')
            plt.locator_params(axis='x', integer=True, tight=True)  # Set x-axis to display integer values and ensure a tight layout
            plt.savefig(f'tag_state_ep{episode+1}_action{action_count}_states.png')
            plt.close()

            # Create a bar plot with columns representing the actions
            plt.figure(dpi=300)
            action_labels = ['Left', 'Right']
            x = [0, 1]
            y = [next_observation[0], next_observation[1]]
            plt.bar(x, y)
            plt.xticks(x, action_labels)
            plt.xlabel('Action')
            plt.ylabel('State Value')
            plt.title(f'Episode {episode+1}, Action {action_count}')
            plt.savefig(f'tag_acts_ep{episode+1}_action{action_count}_action.png')
            plt.close()

        action_count += 1  # Increment the action count

        if done:
            print("Episode {} finished with a reward of {}".format(episode+1, episode_reward))
            break

    # Save the frames as a GIF
    imageio.mimsave(f"run{episode+1}.gif", frames, fps=30)

env.close()  # Close the environment

