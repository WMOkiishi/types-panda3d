from typing import Any, ClassVar, overload
from typing_extensions import Self

from panda3d._typing import Vec3Like
from panda3d.core._express import ReferenceCount
from panda3d.core._linmath import LVecBase3
from panda3d.core._pgraph import NodePath

class AIBehaviors:
    """This class implements all the steering behaviors of the AI framework, such
    as seek, flee, pursue, evade, wander and flock.  Each steering behavior has
    a weight which is used when more than one type of steering behavior is
    acting on the same ai character.  The weight decides the contribution of
    each type of steering behavior.  The AICharacter class has a handle to an
    object of this class and this allows to invoke the steering behaviors via
    the AICharacter.  This class also provides functionality such as pausing,
    resuming and removing the AI behaviors of an AI character at anytime.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: AIBehaviors) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @overload
    def seek(self, pos: Vec3Like, seek_wt: float = ...) -> None:
        """This function activates seek and makes an object of the Seek class.  This
        is the function we want the user to call for seek to be done.  This
        function is overloaded to accept a NodePath or an LVecBase3.
        """
    @overload
    def seek(self, target_object: NodePath, seek_wt: float = ...) -> None: ...
    @overload
    def flee(self, pos: Vec3Like, panic_distance: float = ..., relax_distance: float = ..., flee_wt: float = ...) -> None:
        """This function activates flee_activate and creates an object of the Flee
        class.  This function is overloaded to accept a NodePath or an LVecBase3.
        """
    @overload
    def flee(
        self, target_object: NodePath, panic_distance: float = ..., relax_distance: float = ..., flee_wt: float = ...
    ) -> None: ...
    def pursue(self, target_object: NodePath, pursue_wt: float = ...) -> None:
        """This function activates pursue.  This is the function we want the user to
        call for pursue to be done.
        """
    def evade(
        self, target_object: NodePath, panic_distance: float = ..., relax_distance: float = ..., evade_wt: float = ...
    ) -> None:
        """This function activates evade_activate."""
    def arrival(self, distance: float = ...) -> None:
        """This function activates arrival.  This is the function we want the user to
        call for arrival to be done.
        """
    def flock(self, flock_wt: float) -> None:
        """This function activates flock.  This is the function we want the user to
        call for flock to be done.
        """
    def wander(self, wander_radius: float = ..., flag: int = ..., aoe: float = ..., wander_weight: float = ...) -> None:
        """This function activates wander.  This is the function we want the user to
        call for flock to be done.
        """
    def obstacle_avoidance(self, feeler_length: float = ...) -> None:
        """This function activates obstacle avoidance for a given character.  This is
        the function we want the user to call for obstacle avoidance to be
        performed.
        """
    def path_follow(self, follow_wt: float = ...) -> None:
        """This function activates path following.  This is the function we want the
        user to call for path following.
        """
    def add_to_path(self, pos: Vec3Like) -> None:
        """This function adds positions to the path to follow."""
    def start_follow(self, type: str = ...) -> None: ...
    def init_path_find(self, navmesh_filename: str) -> None:
        """This function activates path finding in the character.  This function
        accepts the meshdata in .csv format.
        """
    @overload
    def path_find_to(self, pos: Vec3Like, type: str = ...) -> None:
        """This function checks for the source and target in the navigation mesh for
        its availability and then finds the best path via the A* algorithm Then it
        calls the path follower to make the object follow the path.
        """
    @overload
    def path_find_to(self, target: NodePath, type: str = ...) -> None: ...
    def add_static_obstacle(self, obstacle: NodePath) -> None:
        """This function allows the user to dynamically add obstacles to the game
        environment.  The function will update the nodes within the bounding volume
        of the obstacle as non-traversable.  Hence will not be considered by the
        pathfinding algorithm.
        """
    def add_dynamic_obstacle(self, obstacle: NodePath) -> None:
        """This function starts the pathfinding obstacle navigation for the passed in
        obstacle.
        """
    def remove_ai(self, ai_type: str) -> None:
        """This function removes individual or all the AIs."""
    def pause_ai(self, ai_type: str) -> None:
        """This function pauses individual or all the AIs."""
    def resume_ai(self, ai_type: str) -> None:
        """This function resumes individual or all the AIs"""
    def behavior_status(self, ai_type: str) -> str:
        """This function returns the status of an AI Type whether it is active, paused
        or disabled.  It returns -1 if an invalid string is passed.
        """
    obstacleAvoidance = obstacle_avoidance
    pathFollow = path_follow
    addToPath = add_to_path
    startFollow = start_follow
    initPathFind = init_path_find
    pathFindTo = path_find_to
    addStaticObstacle = add_static_obstacle
    addDynamicObstacle = add_dynamic_obstacle
    removeAi = remove_ai
    pauseAi = pause_ai
    resumeAi = resume_ai
    behaviorStatus = behavior_status

class AICharacter(ReferenceCount):
    @property
    def name(self) -> str: ...
    @overload
    def __init__(self, __param0: AICharacter) -> None: ...
    @overload
    def __init__(self, model_name: str, model_np: NodePath, mass: float, movt_force: float, max_force: float) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_mass(self) -> float: ...
    def set_mass(self, m: float) -> None: ...
    def get_velocity(self) -> LVecBase3: ...
    def get_max_force(self) -> float: ...
    def set_max_force(self, max_force: float) -> None: ...
    def get_node_path(self) -> NodePath: ...
    def set_node_path(self, np: NodePath) -> None: ...
    def get_ai_behaviors(self) -> AIBehaviors: ...
    def set_pf_guide(self, pf_guide: bool) -> None:
        """This function is used to enable or disable the guides for path finding."""
    getMass = get_mass
    setMass = set_mass
    getVelocity = get_velocity
    getMaxForce = get_max_force
    setMaxForce = set_max_force
    getNodePath = get_node_path
    setNodePath = set_node_path
    getAiBehaviors = get_ai_behaviors
    setPfGuide = set_pf_guide

class AINode:
    """This class is used to assign the nodes on the mesh.  It holds all the data
    necessary to compute A* algorithm.  It also maintains a lot of vital
    information such as the neighbor nodes of each node and also its position
    on the mesh.  Note: The Mesh Generator which is a standalone tool makes use
    of this class to generate the nodes on the mesh.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: AINode) -> None: ...
    @overload
    def __init__(self, grid_x: int, grid_y: int, pos: Vec3Like, w: float, l: float, h: float) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def contains(self, x: float, y: float) -> bool:
        """This is a handy function which returns true if the passed position is
        within the node's dimensions.
        """

class Flock:
    """This class is used to define the flock attributes and the AI characters
    which are part of the flock.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: Flock) -> None: ...
    @overload
    def __init__(
        self,
        flock_id: int,
        vcone_angle: float,
        vcone_radius: float,
        separation_wt: int = ...,
        cohesion_wt: int = ...,
        alignment_wt: int = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def add_ai_char(self, ai_char: AICharacter) -> None:
        """This function adds AI characters to the flock."""
    def get_id(self) -> int:
        """Function to access the private member flock_id."""
    addAiChar = add_ai_char
    getId = get_id

class AIWorld:
    """A class that implements the virtual AI world which keeps track of the AI
    characters active at any given time.  It contains a linked list of AI
    characters, obstactle data and unique name for each character.  It also
    updates each characters state.  The AI characters can also be added to the
    world as flocks.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: AIWorld) -> None: ...
    @overload
    def __init__(self, render: NodePath) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def add_ai_char(self, ai_ch: AICharacter) -> None: ...
    def remove_ai_char(self, name: str) -> None: ...
    def add_flock(self, flock: Flock) -> None:
        """This function adds all the AI characters in the Flock object to the
        AICharPool.  This function allows adding the AI characetrs as part of a
        flock.
        """
    def flock_off(self, flock_id: int) -> None:
        """This function turns off the flock behavior temporarily.  Similar to pausing
        the behavior.
        """
    def flock_on(self, flock_id: int) -> None:
        """This function turns on the flock behavior."""
    def remove_flock(self, flock_id: int) -> None:
        """This function removes the flock behavior completely."""
    def get_flock(self, flock_id: int) -> Flock:
        """This function returns a handle to the Flock whose id is passed."""
    def add_obstacle(self, obstacle: NodePath) -> None:
        """This function adds the nodepath as an obstacle that is needed by the
        obstacle avoidance behavior.
        """
    def remove_obstacle(self, obstacle: NodePath) -> None:
        """This function removes the nodepath from the obstacles list that is needed
        by the obstacle avoidance behavior.
        """
    def print_list(self) -> None:
        """This function prints the names of the AI characters that have been added to
        the AIWorld.  Useful for debugging purposes.
        """
    def update(self) -> None:
        """The AIWorld update function calls the update function of all the AI
        characters which have been added to the AIWorld.
        """
    addAiChar = add_ai_char
    removeAiChar = remove_ai_char
    addFlock = add_flock
    flockOff = flock_off
    flockOn = flock_on
    removeFlock = remove_flock
    getFlock = get_flock
    addObstacle = add_obstacle
    removeObstacle = remove_obstacle
    printList = print_list
